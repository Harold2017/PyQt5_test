import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser, QLineEdit
from password_dialog import PasswordDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(380, 180)
        self.setWindowTitle('Learn PyQt5')

        self.lb = QLabel('Password shown here', self)
        self.lb.move(20, 20)

        self.btn_normal = QPushButton('Input password(Normal): ', self)
        self.btn_normal.move(20, 60)

        self.btn_enhanced = QPushButton('Input password(Enhanced): ', self)
        self.btn_enhanced.move(20, 100)

        self.btn_super_enhanced = QPushButton('Input password(SuperEnhanced): ', self)
        self.btn_super_enhanced.move(20, 140)

        self.show()

        self.btn_normal.clicked.connect(self.showDialog)
        self.btn_enhanced.clicked.connect(self.showDialog)
        self.btn_super_enhanced.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        if sender == self.btn_normal:
            text, ok = QInputDialog.getText(self, 'Password Input Dialog', 'Please input password: ', QLineEdit.Password)
            if ok:
                self.lb.setText(text)
        elif sender == self.btn_enhanced:
            text, ok = QInputDialog.getText(self, 'Password Input Dialog', 'Please input password: ', QLineEdit.PasswordEchoOnEdit)
            if ok:
                self.lb.setText(text)
        else:
            pwd = PasswordDialog()
            r = pwd.exec_()
            # print(r)
            # print(pwd.text)
            if r:
                self.lb.setText(pwd.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
