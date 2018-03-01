import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Learn PyQt5')

        formlayout = QFormLayout()
        nameLabel = QLabel('Name')
        nameLineEdit = QLineEdit('')
        introductionLabel = QLabel('Introduction')
        introductionLineEdit = QTextEdit('')

        formlayout.addRow(nameLabel, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLineEdit)

        self.setLayout(formlayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
