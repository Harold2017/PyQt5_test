import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.initUi()
        # with setMouseTracking(True), mouse pattern will be tracked with pressing
        # self.setMouseTracking(True)

    def initUi(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('Learn PyQt5')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, e):
        distance_from_center = round(((e.y() - 250)**2 + (e.x() - 500)**2)**0.5)
        self.label.setText('Coordinate: (x: {0}, y: {1})'.format(e.x(), e.y()) +
                           'Distance from center: {0}'.format(distance_from_center))
        self.pos = e.pos()
        # .update() to update graph
        self.update()

    def paintEvent(self, e):
        if self.pos:
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
