import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Learn PyQt5--Guess Numbers')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.btn = QPushButton('Guss', self)
        self.btn.setGeometry(115, 150, 70, 30)
        self.btn.setToolTip('<b>Click here to guess</b>')
        self.btn.clicked.connect(self.showMessage)

        self.text = QLineEdit('Input a number here', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):
        guessnumber = int(self.text.text())
        print(self.num)

        if guessnumber > self.num:
            QMessageBox.about(self, 'Oh', 'larger!')
            self.text.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, 'Oh', 'smaller')
            self.text.setFocus()
        else:
            QMessageBox.about(self, 'You got the right answer!', 'Go to next round!')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm', 'Are you sure to quit now?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
