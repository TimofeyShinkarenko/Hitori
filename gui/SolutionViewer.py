from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, \
    QPushButton, QLabel
from .TwoFieldsWidget import TwoFieldsWidget


class SolutionViewer(QMainWindow):
    def __init__(self, data_list, cell_size=50):
        super().__init__()
        self.setWindowTitle("Hitori Solutions Viewer")
        self.data_list = data_list
        self.cell_size = cell_size
        self.current_task_index = 0

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        if len(self.data_list) > 1:
            self.task_nav_layout = QHBoxLayout()

            self.btn_prev_task = QPushButton("<< Предыдущее поле")
            self.btn_prev_task.clicked.connect(self.prev_task)
            self.btn_prev_task.setEnabled(False)

            self.lbl_task_counter = QLabel(f"Поле 1 из {len(self.data_list)}")

            self.btn_next_task = QPushButton("Следующее поле >>")
            self.btn_next_task.clicked.connect(self.next_task)

            self.task_nav_layout.addWidget(self.btn_prev_task)
            self.task_nav_layout.addStretch()
            self.task_nav_layout.addWidget(self.lbl_task_counter)
            self.task_nav_layout.addStretch()
            self.task_nav_layout.addWidget(self.btn_next_task)

            self.main_layout.addLayout(self.task_nav_layout)

        self.task_container = QVBoxLayout()
        self.main_layout.addLayout(self.task_container)

        self.show_current_task()
        self.resize(800, 600)

    def show_current_task(self):
        while self.task_container.count():
            item = self.task_container.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        original_field, solutions = self.data_list[self.current_task_index]

        two_fields_widget = TwoFieldsWidget(self.cell_size, original_field,
                                            solutions)
        self.task_container.addWidget(two_fields_widget)

    def prev_task(self):
        if self.current_task_index > 0:
            self.current_task_index -= 1
            self.update_nav_buttons()
            self.show_current_task()

    def next_task(self):
        if self.current_task_index < len(self.data_list) - 1:
            self.current_task_index += 1
            self.update_nav_buttons()
            self.show_current_task()

    def update_nav_buttons(self):
        self.lbl_task_counter.setText(
            f"Поле {self.current_task_index + 1} из {len(self.data_list)}")
        self.btn_prev_task.setEnabled(self.current_task_index > 0)
        self.btn_next_task.setEnabled(
            self.current_task_index < len(self.data_list) - 1)