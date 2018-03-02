import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QDialog
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.printer = QPrinter()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Learn PyQt5')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.btn_file = QPushButton('Open file', self)
        self.btn_file.move(350, 20)

        self.btn_files = QPushButton('Open multiple files', self)
        self.btn_files.move(350, 70)

        self.btn_save = QPushButton('Save file', self)
        self.btn_save.move(350, 220)

        self.btn_pagesetup = QPushButton('Page setup', self)
        self.btn_pagesetup.move(350, 270)

        self.btn_print = QPushButton('Print file', self)
        self.btn_print.move(350, 320)

        self.btn_file.clicked.connect(self.openfile)
        self.btn_files.clicked.connect(self.openfiles)
        self.btn_save.clicked.connect(self.save)
        self.btn_pagesetup.clicked.connect(self.pagesetup)
        self.btn_print.clicked.connect(self.printdialog)

        self.show()

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.tx.setText(f.read())

    def openfiles(self):
        fnames = QFileDialog.getOpenFileNames(self, 'Open multiple files', './')
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
                    self.tx.append(f.read())

    def save(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file', './', "Text files (*.txt)")
        if fname[0]:
            with open(fname[0], 'w', encoding='utf-8', errors='ignore') as f:
                f.write(self.tx.toPlainText())

    def pagesetup(self):
        setupdialog = QPageSetupDialog(self.printer, self)
        setupdialog.exec_()

    def printdialog(self):
        printdialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printdialog.exec_():
            self.tx.print(self.printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
