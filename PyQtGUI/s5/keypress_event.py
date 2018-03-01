import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Learn PyQt5')

        self.lab = QLabel('Direction', self)
        self.lab.setGeometry(150, 100, 50, 50)

        self.show()

    def keyPressEvent(self, e):
        qt_keys = {Qt.Key_Up: '↑',
                   Qt.Key_Down: '↓',
                   Qt.Key_Left: '←',
                   Qt.Key_Right: '→'}
        self.lab.setText(qt_keys.get(e.key()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
