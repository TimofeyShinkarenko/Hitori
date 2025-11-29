from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QDialog


class NumberInputDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Введите два числа")
        self.setFixedSize(250, 150)

        layout = QVBoxLayout()

        h1 = QHBoxLayout()
        h1.addWidget(QLabel("Ширина:"))
        self.num1 = QLineEdit()
        self.num1.setPlaceholderText("Введите число")
        h1.addWidget(self.num1)
        layout.addLayout(h1)

        h2 = QHBoxLayout()
        h2.addWidget(QLabel("Высота:"))
        self.num2 = QLineEdit()
        self.num2.setPlaceholderText("Введите число")
        h2.addWidget(self.num2)
        layout.addLayout(h2)

        self.ok_btn = QPushButton("OK")
        self.ok_btn.clicked.connect(self.accept)
        layout.addWidget(self.ok_btn)

        self.setLayout(layout)

    def get_values(self):
        """Вернуть два введённых числа (или None, если не число)."""
        try:
            return int(self.num1.text()), int(self.num2.text())
        except ValueError:
            return None, None