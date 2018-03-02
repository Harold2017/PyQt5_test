import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap


import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('Learn PyQt5')

        self.lb = QLabel('Information                                            ', self)
        self.lb.move(20, 20)

        self.btn_info = QPushButton('Info', self)
        self.btn_info.move(20, 70)

        self.btn_question = QPushButton('Question', self)
        self.btn_question.move(120, 70)

        self.btn_warning = QPushButton('Warning', self)
        self.btn_warning.move(220, 70)

        self.btn_critical = QPushButton('Critical', self)
        self.btn_critical.move(20, 140)

        self.btn_about = QPushButton('About', self)
        self.btn_about.move(120, 140)

        self.btn_about_qt = QPushButton('About Qt', self)
        self.btn_about_qt.move(220, 140)

        self.btn_info.clicked.connect(self.info)
        self.btn_question.clicked.connect(self.question)
        self.btn_warning.clicked.connect(self.warning)
        self.btn_critical.clicked.connect(self.critical)
        self.btn_about.clicked.connect(self.about)
        self.btn_about_qt.clicked.connect(self.about_qt)

        self.show()

    def info(self):
        # QMessageBox.information(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons,
        # QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton =
        # MessageBox.NoButton)
        reply = QMessageBox.information(self, 'Info', 'A infomation messagebox!',
                                        QMessageBox.Ok | QMessageBox.Close,
                                        QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.lb.setText('You choose Ok!')
        else:
            self.lb.setText('You choose Close!')

    def question(self):
        reply = QMessageBox.question(self, 'Query', 'A question messagebox, default is No.',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.lb.setText('You choose Yes!')
        elif reply == QMessageBox.No:
            self.lb.setText('You choose No!')
        else:
            self.lb.setText('You choose Cancel!')

    def warning(self):
        # reply = QMessageBox.warning(self,'Warning','A warning message dialog!', QMessageBox.Save |
        # QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
        cb = QCheckBox('Apply this operation on all files.')
        msgbox = QMessageBox()
        msgbox.setWindowTitle('Warning')
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText('A warning messagebox')
        msgbox.setInformativeText('Will you intend to save changes')
        save = msgbox.addButton('Save', QMessageBox.AcceptRole)
        notsave = msgbox.addButton('Not save', QMessageBox.RejectRole)
        cancel = msgbox.addButton('Cancel', QMessageBox.DestructiveRole)
        msgbox.setDefaultButton(save)
        msgbox.setCheckBox(cb)
        cb.stateChanged.connect(self.check)
        reply = msgbox.exec_()
        if reply == QMessageBox.AcceptRole:
            self.lb.setText('You choose to save changes!')
        elif reply == QMessageBox.RejectRole:
            self.lb.setText('You choose to not save changes!')
        else:
            self.lb.setText('You choose to cancel!')

    def critical(self):
        # reply = QMessageBox.critical(self,'Critical','A critical messagebox',
        # QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore , QMessageBox.Retry)
        msgbox = QMessageBox()
        msgbox.setWindowTitle('Critical')
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.setText('A critical messagebox')
        # standard buttons shown on messagebox
        msgbox.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore)
        msgbox.setDefaultButton(QMessageBox.Retry)
        # details property to show details
        msgbox.setDetailedText('Detailed information: Fuck it!')
        reply = msgbox.exec_()

        if reply == QMessageBox.Retry:
            self.lb.setText('You choose to retry!')
        elif reply == QMessageBox.Abort:
            self.lb.setText('You choose to abort!')
        else:
            self.lb.setText('You choose to ignore')

    def about(self):
        # QMessageBox.about(self,'About','A about messagebox!')
        msgbox = QMessageBox(QMessageBox.NoIcon, 'About', 'Do Not fantasy, please wash yourself and sleep!')
        msgbox.setIconPixmap(QPixmap('motou.png'))
        msgbox.exec_()

    def about_qt(self):
        QMessageBox.aboutQt(self, 'About Qt')

    def check(self):
        if self.sender().isChecked():
            self.lb.setText('You tick.')
        else:
            self.lb.setText('Why not tick now?')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
