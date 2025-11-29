from PyQt5.QtWidgets import QFrame, QGridLayout

from game.field import Field
from interface.UI.CellWidget import CellWidget


class FieldWidget(QFrame):
    def __init__(self, size, field: Field):
        super().__init__()
        width = field.width
        height = field.height
        self.setFrameShape(QFrame.Box)
        self.setFixedSize(size * height + 4, size * width + 4)

        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        for i in range(width):
            for j in range(height):
                cell = CellWidget(size)
                cell.set_number(field.cells[i][j].value)
                if not field.cells[i][j].is_unpainted:
                    cell.fill()
                layout.addWidget(cell, i, j)

        self.setLayout(layout)