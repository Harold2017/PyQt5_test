import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Learn PyQt5')

        # absolute coordinate layout
        btn1 = QPushButton('Button one', self)
        btn1.move(50, 250)

        btn2 = QPushButton('Button two', self)
        btn2.move(150, 250)

        btn3 = QPushButton('Button three', self)
        btn3.move(250, 250)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
