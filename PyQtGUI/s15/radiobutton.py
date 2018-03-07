import sys
from PyQt5.QtWidgets import QWidget, QRadioButton, QApplication, QPushButton, QMessageBox, QButtonGroup, \
    QHBoxLayout, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.rbtn11 = QRadioButton('You are', self)
        self.rbtn12 = QRadioButton('I am', self)
        self.rbtn13 = QRadioButton('He(She) is', self)
        self.rbtn21 = QRadioButton('beautiful', self)
        self.rbtn22 = QRadioButton('handsome', self)
        self.rbtn23 = QRadioButton('foolish', self)

        btn = QPushButton('Submit', self)

        vbl = QVBoxLayout()
        vbl.addWidget(self.rbtn11)
        vbl.addStretch(1)
        vbl.addWidget(self.rbtn12)
        vbl.addStretch(1)
        vbl.addWidget(self.rbtn13)
        vbl.addStretch(1)

        vbl2 = QVBoxLayout()
        vbl2.addWidget(self.rbtn21)
        vbl2.addStretch(1)
        vbl2.addWidget(self.rbtn22)
        vbl2.addStretch(1)
        vbl2.addWidget(self.rbtn23)
        vbl2.addStretch(1)

        hbl = QHBoxLayout()
        hbl.addLayout(vbl)
        hbl.addStretch(1)
        hbl.addLayout(vbl2)
        hbl.addStretch(1)

        vbl3 = QVBoxLayout()
        vbl3.addLayout(hbl)
        vbl3.addStretch(1)
        vbl3.addWidget(btn)
        vbl3.addStretch(1)

        self.setLayout(vbl3)
        self.show()

        self.info1 = ''
        self.info2 = ''

        # if not add radiobutton into button group, they are all exclusive
        # due to radiobutton is autoExclusive
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.rbtn11, 11)
        self.bg1.addButton(self.rbtn12, 12)
        self.bg1.addButton(self.rbtn13, 13)

        self.bg2 = QButtonGroup(self)
        # prototype in C++: QButtonGroup.addButton(self, QAbstractButton, id: int = -1)
        # auto distributed id is negative, use positive int for user defined id
        self.bg2.addButton(self.rbtn21, 21)
        self.bg2.addButton(self.rbtn22, 22)
        self.bg2.addButton(self.rbtn23, 23)

        # button in button group will emit buttonClicked signal when it is clicked
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bg2.buttonClicked.connect(self.rbclicked)
        btn.clicked.connect(self.submit)

    def submit(self):
        if self.info1 == '' and self.info2 == '':
            QMessageBox.information(self, 'What?', 'You choose nothing!')
        else:
            QMessageBox.information(self, 'What?', self.info1 + self.info2)

    def rbclicked(self):
        # self.sender() will send the object which sends the signal
        sender = self.sender()
        outDict = {11: 'You are ',
                   12: 'I am ',
                   13: 'He(She) is ',
                   21: 'beautiful',
                   22: 'handsome',
                   23: 'foolish'}
        # use checkedId() to obtain the button's id
        if sender == self.bg1:
            # TypeError: get() takes no keyword arguments
            # so cannot use default = ''
            self.info1 = outDict.get(self.bg1.checkedId(), '')
        else:
            self.info2 = outDict.get(self.bg2.checkedId(), '')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
