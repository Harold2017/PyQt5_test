import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Learn PyQt5')
        self.setWindowIcon(QIcon('favicon.ico'))

        qbtn = QPushButton('Exit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(70, 30)
        qbtn.move(50, 50)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())
