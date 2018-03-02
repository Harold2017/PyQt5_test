import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Learn PyQt5')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.btn_file = QPushButton('Open file', self)
        self.btn_file.move(350, 20)

        self.btn_font = QPushButton('Choose font', self)
        self.btn_font.move(350, 70)

        self.btn_color = QPushButton('Choose color', self)
        self.btn_color.move(350, 120)

        self.btn_file.clicked.connect(self.openfile)
        self.btn_font.clicked.connect(self.choosefont)
        self.btn_color.clicked.connect(self.choosecolor)

        self.show()

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.tx.setText(f.read())

    def choosefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)

    def choosecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
