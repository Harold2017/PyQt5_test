from testgui import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox
import sys
from random import randint


class Action(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Action, self).__init__()
        self.setupUi(self)
        self.num = randint(1, 100)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """Slot"""
        guessnumber = int(self.lineEdit.text())
        print(self.num)
        if guessnumber > self.num:
            QMessageBox.about(self, 'Result', 'Too large!')
        elif guessnumber < self.num:
            QMessageBox.about(self, 'Result', 'Too small!')
        else:
            QMessageBox.about(self, 'Result', 'Correct! Go to next round!')
            self.num = randint(1, 100)
            self.lineEdit.clear()
            self.lineEdit.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Action()
    window.show()
    sys.exit(app.exec_())
