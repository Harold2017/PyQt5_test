import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Learn PyQt5')

        btn1 = QPushButton('button 1', self)
        btn2 = QPushButton('button 2', self)
        btn3 = QPushButton('button 3', self)

        # create a horizontal layout box
        hbox = QHBoxLayout()
        # create stretch spacer
        # number in addStretch function means the number of stretch spacer(QSpacerItem)
        # this spacer is arranged from left to right
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addStretch(1)
        hbox.addWidget(btn2)
        hbox.addStretch(1)
        hbox.addWidget(btn3)
        hbox.addStretch(6)

        # create a vertical layout box
        vbox = QVBoxLayout()
        # ceate stretch spacer
        # this spacer is arranged from top to bottom
        vbox.addStretch(1)
        # put horizontal layout box in this vertical layout box
        vbox.addLayout(hbox)
        vbox.addStretch(2)

        self.setLayout(vbox)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
