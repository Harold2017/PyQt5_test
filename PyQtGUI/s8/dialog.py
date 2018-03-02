import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(500, 500, 500, 550)
        self.setWindowTitle('Learn PyQt5')

        self.lb_name = QLabel('Name: ', self)
        self.lb_name.move(20, 20)

        self.lb_age = QLabel('Age: ', self)
        self.lb_age.move(20, 80)

        self.lb_sex = QLabel('Sex: ', self)
        self.lb_sex.move(20, 140)

        self.lb_height = QLabel('Height: ', self)
        self.lb_height.move(20, 200)

        self.lb_info = QLabel('Basic Information: ', self)
        self.lb_info.move(20, 260)

        self.lb_name_default = QLabel('Py          ', self)
        self.lb_name_default.move(80, 20)

        self.lb_age_default = QLabel('18          ', self)
        self.lb_age_default.move(80, 80)

        self.lb_sex_default = QLabel('Secure', self)
        self.lb_sex_default.move(80, 140)

        self.lb_height_default = QLabel('170     ', self)
        self.lb_height_default.move(80, 200)

        self.lb_info_default = QTextBrowser(self)
        self.lb_info_default.move(20, 320)

        self.bt_name = QPushButton('Edit name', self)
        self.bt_name.move(200, 20)

        self.bt_age = QPushButton('Edit age', self)
        self.bt_age.move(200, 80)

        self.bt_sex = QPushButton('Edit sex', self)
        self.bt_sex.move(200, 140)

        self.bt_height = QPushButton('Edit height', self)
        self.bt_height.move(200, 200)

        self.bt_info = QPushButton('Edit information', self)
        self.bt_info.move(200, 260)

        self.show()

        self.bt_name.clicked.connect(self.showDialog)
        self.bt_age.clicked.connect(self.showDialog)
        self.bt_sex.clicked.connect(self.showDialog)
        self.bt_height.clicked.connect(self.showDialog)
        self.bt_info.clicked.connect(self.showDialog)


    def showDialog(self):
        sender = self.sender()
        sex = ['Secure', 'Male', 'Female']
        if sender == self.bt_name:
            """getText(QWidget, str, str, echo: QLineEdit.EchoMode = QLineEdit.Normal,text: str = '', flags: Union[
            Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(),inputMethodHints: Union[Qt.InputMethodHints, 
            Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool] """
            text, ok = QInputDialog.getText(self, 'Edit name', 'Please input your name: ')
            if ok:
                self.lb_name_default.setText(text)
        elif sender == self.bt_age:
            """getInt(QWidget, str, str, value: int = 0, min: int = -2147483647, max: int = 2147483647, step: int = 
            1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[int, bool] """
            text, ok = QInputDialog.getInt(self, 'Edit age', 'Please input your age: ', min=1)
            if ok:
                self.lb_age_default.setText(str(text))
        elif sender == self.bt_sex:
            """getItem(QWidget, str, str, Iterable[str], current:int=0,editable:bool=True,flags:Union[Qt.WindowFlags,
            Qt.WindowType]=Qt.WindowFlags(),inputMethodHints:Union[Qt.InputMethodHints,Qt.InputMethodHint] = 
            Qt.ImhNone) -> Tuple[str, bool] """
            text, ok = QInputDialog.getItem(self, 'Edit sex', 'Please input your choose your sex: ', sex)
            if ok:
                self.lb_sex_default.setText(text)
        elif sender == self.bt_height:
            """getDouble(QWidget, str, str, value: float = 0, min: float = -2147483647, max: float = 2147483647, 
            decimals: int = 1, flags: Union[Qt.WindowFlags,Qt.WindowType]=Qt.WindowFlags())->Tuple[float,bool] """
            text, ok = QInputDialog.getDouble(self, 'Edit height', 'Please input your height: ', min=1.0)
            if ok:
                self.lb_height_default.setText(str(text))
        elif sender == self.bt_info:
            """getMultiLineText(QWidget, str, str, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = 
            Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone)-> Tuple[
            str, bool] """
            text, ok = QInputDialog.getMultiLineText(self, 'Edit information',
                                                     'Please input your personal information: ')
            if ok:
                self.lb_info_default.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
