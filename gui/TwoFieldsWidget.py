from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

from game.field import Field
from .FieldWidget import FieldWidget


class TwoFieldsWidget(QWidget):
    def __init__(self, cell_size, field: Field, solutions: list[Field]):
        super().__init__()
        self.index = 0
        self.solutions_count = len(solutions)
        self.solutions = solutions
        self.cell_size = cell_size

        self.left_field = FieldWidget(cell_size, field)
        self.right_field = QLabel("Нет решений")
        self.central_label = QLabel('')
        if self.solutions_count > 0:
            self.right_field = FieldWidget(cell_size, self.solutions[self.index])
            self.central_label = QLabel(f"{self.index + 1}/{self.solutions_count}")

        self.central_container = QVBoxLayout()
        self.central_container.addWidget(self.central_label)


        self.top_row = QHBoxLayout()
        self.top_row.addWidget(self.left_field)
        self.right_container = QVBoxLayout()
        self.right_container.addWidget(self.right_field)
        self.top_row.addLayout(self.right_container)

        self.next_button = QPushButton("След. решение")
        self.next_button.setFixedHeight(40)
        self.next_button.clicked.connect(self.next_button_clicked)

        self.prev_button = QPushButton("Пред. решение")
        self.prev_button.setFixedHeight(40)
        self.prev_button.clicked.connect(self.prev_button_clicked)
        self.prev_button.setEnabled(False)

        bottom_row = QHBoxLayout()
        bottom_row.addWidget(self.prev_button)
        bottom_row.addStretch()
        bottom_row.addWidget(self.next_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.top_row)
        main_layout.addStretch()
        main_layout.addLayout(self.central_container)
        main_layout.addLayout(bottom_row)
        self.setLayout(main_layout)


    def next_button_clicked(self):
        self.index += 1
        if self.index == self.solutions_count - 1:
            self.next_button.setEnabled(False)
        if self.index > 0:
            self.prev_button.setEnabled(True)
        self.replace_right_grid()


    def prev_button_clicked(self):
        self.index -= 1
        if self.index < self.solutions_count - 1:
            self.next_button.setEnabled(True)
        if self.index == 0:
            self.prev_button.setEnabled(False)
        self.replace_right_grid()

    def replace_right_grid(self):
        old_widget = self.right_field
        old_widget.setParent(None)
        self.right_field = FieldWidget(self.cell_size, self.solutions[self.index])
        self.right_container.addWidget(self.right_field)

        old_label = self.central_label
        old_label.setParent(None)
        self.central_label = QLabel(f"{self.index + 1}/{self.solutions_count}")
        self.central_container.addWidget(self.central_label)