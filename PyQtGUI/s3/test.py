from testgui import Ui_MainWindow  # 导入testgui.ui转换为testgui.py中的类 (pyuic5 -o .py .ui)

from PyQt5 import QtWidgets
import sys


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())
