import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject


class Signal(QObject):
    # use pyqtSignal() to create a signal and bind it to class Signal's attribute showmouse
    showmouse = pyqtSignal()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Learn PyQt5')

        self.s = Signal()
        # connect user defined showmouse signal to about slot of MainWindow
        self.s.showmouse.connect(self.about)

        self.show()

    # about slot of MainWindow
    def about(self):
        QMessageBox.about(self, 'Mouse', 'You press mouse!')

    def mousePressEvent(self, e):
        # call emit function of signal and since the signal is bond to about slot
        # the slot will be called
        self.s.showmouse.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
