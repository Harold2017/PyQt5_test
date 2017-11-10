import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QDesktopWidget, QFileDialog
from PyQt5.QtGui import QIcon


class Note(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        saveAct = QAction(QIcon('save.png'), '&Save file', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save file')
        saveAct.triggered.connect(self.file_save)

        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

        toolbar_new = self.addToolBar('Save')
        toolbar_new.addAction(saveAct)
        toolbar_exit = self.addToolBar('Exit')
        toolbar_exit.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.center()

        self.setWindowTitle('Note')
        self.show()

    def file_save(self):
        name, _ = QFileDialog.getSaveFileName(self, 'Save file', "", "Text Files(*.txt);;All Files(*)")
        if name:
            print(name)
            file = open(name, 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
        else:
            return False

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Note()
    sys.exit(app.exec_())
