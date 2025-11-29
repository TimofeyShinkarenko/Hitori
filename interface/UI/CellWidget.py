from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QWidget


class CellWidget(QWidget):
    def __init__(self, size):
        super().__init__()
        self.number = 0
        self.filled = False
        self.setFixedSize(size, size)

    def set_number(self, num):
        self.number = num
        self.filled = False
        self.update()

    def fill(self):
        self.number = None
        self.filled = True
        self.update()


    '''
    #просто прикольно было потыкаться
    def mousePressEvent(self, event):
        if not self.filled:
            self.filled = True
        else:
            self.filled = False
        self.update()'''

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 1))
        painter.drawRect(self.rect())

        if self.filled:
            painter.fillRect(self.rect(), Qt.black)

        painter.setFont(QFont("Arial", 14))
        painter.drawText(self.rect(), Qt.AlignCenter, str(self.number))