import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QAction, QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar, QFileDialog, QWidget, QFrame, QHBoxLayout, QGridLayout, QVBoxLayout, QPushButton,
    QInputDialog
)

from interface.UI.NumberInputDialog import NumberInputDialog
from solver import Solver
from interface.parser import Parser
from TwoFieldsWidget import TwoFieldsWidget
from generate.field_generator import FieldGenerator

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.cell_size = 50
        self.solutions = None
        self.original_hitori = None
        self.max_solves = 5
        self.num_components = 1

        self.setWindowTitle("Hitori")
        self.resize(800, 500)
        self.create_menu()


    def create_menu(self):
        file_button_action = QAction("Open file", self)
        file_button_action.triggered.connect(self.open_file)

        max_solves_action = QAction("Max Solves", self)
        max_solves_action.triggered.connect(self.set_max_solves)

        num_components_action = QAction("Number of Components", self)
        num_components_action.triggered.connect(self.set_num_components)

        generate_action = QAction("Generate Hitori", self)
        generate_action.triggered.connect(self.generate_hitori)

        menu = self.menuBar()

        menu.addAction(file_button_action)
        menu.addAction(max_solves_action)
        menu.addAction(num_components_action)
        menu.addAction(generate_action)


    def generate_hitori(self):
        dialog = NumberInputDialog()

        if dialog.exec_():
            width, height = dialog.get_values()
            try:
                self.original_hitori = FieldGenerator(height, width).generate_field()
                self.solutions = list(Solver(self.max_solves, self.num_components, field= self.original_hitori).solve())
                self.setCentralWidget(TwoFieldsWidget(self.cell_size, self.original_hitori, self.solutions))
            except Exception as e:
                label = QLabel(str(e))
                label.setFont(QFont("Arial", 20))
                self.setCentralWidget(label)


    def set_num_components(self):
        self.num_components, ok = QInputDialog.getInt(self, "Введите максимальное количество компонент связности",
                                    "Количество компонент связности", self.num_components, 0, 10000, 1)

    def set_max_solves(self):
        self.max_solves, ok = QInputDialog.getInt(self, "Введите максимальное количество решений",
                                    "Количество решений", self.max_solves, 0, 10000, 1)

    def open_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Выберите файл")
        if filepath:
            with open(filepath, "r") as file:
                lines = file.readlines()
                try:
                    self.original_hitori = Parser.parse_lines_to_field(lines)
                    self.solutions = list(Solver(self.max_solves, self.num_components, filepath).solve())
                    self.setCentralWidget(TwoFieldsWidget(self.cell_size, self.original_hitori, self.solutions))
                except Exception as e:
                    label = QLabel(str(e))
                    label.setFont(QFont("Arial", 20))
                    self.setCentralWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
