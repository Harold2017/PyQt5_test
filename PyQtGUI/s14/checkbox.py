import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(300, 500)
        self.setWindowTitle('Learn PyQt5')

        self.cb_all = QCheckBox('Select all', self)
        self.cb_1 = QCheckBox('You are', self)
        self.cb_2 = QCheckBox('my', self)
        self.cb_3 = QCheckBox('little apple', self)

        btn = QPushButton('Submit', self)

        vbl = QVBoxLayout()
        vbl.addStretch(1)
        vbl.addWidget(self.cb_1)
        vbl.addStretch(1)
        vbl.addWidget(self.cb_2)
        vbl.addStretch(1)
        vbl.addWidget(self.cb_3)
        vbl.addStretch(1)
        vbl.addWidget(btn)
        vbl.addStretch(1)

        hbl = QHBoxLayout()
        hbl.addWidget(self.cb_all)
        hbl.addStretch(1)
        hbl.addLayout(vbl)
        hbl.addStretch(1)

        self.setLayout(hbl)

        self.show()

        self.cb_all.stateChanged.connect(self.changecb_all)
        self.cb_1.stateChanged.connect(self.changecb)
        self.cb_2.stateChanged.connect(self.changecb)
        self.cb_3.stateChanged.connect(self.changecb)

        btn.clicked.connect(self.go)

    def go(self):
        checkList = list(map(str, map(int, [self.cb_1.isChecked(),
                                   self.cb_2.isChecked(),
                                   self.cb_3.isChecked()])))
        checkList = ''.join(checkList)
        # print(checkList)
        outDict = {'111': ['Love you baby', 'You are my little apple!'],
                   '110': ['Love you baby', 'You are mine!'],
                   '101': ['Love you baby', 'You are little apple!'],
                   '100': ['Love you baby', 'You are!'],
                   '011': ['Love you baby', 'My little apple!'],
                   '010': ['Love you baby', 'Mine!'],
                   '001': ['Love you baby', 'little apple!'],
                   '000': ['Love you baby', 'You choose nothing, my girl!']}
        outString = outDict.get(checkList)
        # print(outString)
        QMessageBox.information(self, outString[0], outString[1])

    def changecb_all(self):
        if self.cb_all.checkState() == Qt.Checked:
            self.cb_1.setChecked(True)
            self.cb_2.setChecked(True)
            self.cb_3.setChecked(True)
        elif self.cb_all.checkState() == Qt.Unchecked:
            self.cb_1.setChecked(False)
            self.cb_2.setChecked(False)
            self.cb_3.setChecked(False)

    def changecb(self):
        if self.cb_1.isChecked() and self.cb_2.isChecked() and self.cb_3.isChecked():
            self.cb_all.setCheckState(Qt.Checked)
        elif self.cb_1.isChecked() or self.cb_2.isChecked() or self.cb_3.isChecked():
            self.cb_all.setTristate()
            self.cb_all.setCheckState(Qt.PartiallyChecked)
        else:
            self.cb_all.setTristate(False)
            self.cb_all.setCheckState(Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
