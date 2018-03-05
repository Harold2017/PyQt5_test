import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(300, 150)
        self.setWindowTitle('Learn PyQt5')

        self.lb = QLabel('File numbers', self)
        self.lb.move(20, 40)

        self.btn_start = QPushButton('Start', self)
        self.btn_start.move(20, 80)

        self.edit = QLineEdit('100000', self)
        self.edit.move(100, 40)

        self.show()

        self.btn_start.clicked.connect(self.showDialog)

    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle('Please wait for a while')
        progress.setLabelText('Operating...')
        progress.setCancelButtonText('Cancel')
        progress.setMinimumDuration(5)
        # reference: http://pyqt.sourceforge.net/Docs/PyQt4/qprogressdialog.html
        # Qt.NonModal: window is not modal and it will not block other windows' inputs (default)
        # Qt.WindowModa: window is modal for single layer and block its parent / brother windows' inputs
        # Qt.ApplicationModal: window is modal for application and block all other windows' inputs
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0, num)
        # For loops also have an else clause which most of us are unfamiliar with.
        # The else clause executes when the loop completes normally.
        # This means that the loop did not encounter any break.
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self, 'Hint', 'Operation Failed')
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, 'Hint', 'Operation Succeeded')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
