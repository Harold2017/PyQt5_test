from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, \
    QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
import sys


class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(350, 100)
        self.setWindowTitle('Password Input Dialog')

        self.lb = QLabel('Please input password: ', self)

        self.edit = QLineEdit(self)
        # install event filter
        # if install multiple event filters on one object, the last one will be activated first
        self.edit.installEventFilter(self)

        self.btn_confirm = QPushButton('Confirm', self)
        self.btn_cancel = QPushButton('Cancel', self)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.lb)
        vbox.addStretch(1)
        vbox.addWidget(self.edit)
        vbox.addStretch(1)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn_confirm)
        hbox.addStretch(1)
        hbox.addWidget(self.btn_cancel)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

        # set no context -> disable right click menu
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        # placeholder as hint
        self.edit.setPlaceholderText('Password length 6-15, only numbers and letters valid, start with letter')
        # confine display format
        self.edit.setEchoMode(QLineEdit.Password)

        regx = QRegExp('^[a-zA-Z][0-9a-zA-Z]{14}$')
        validator = QRegExpValidator(regx, self.edit)
        self.edit.setValidator(validator)

        self.btn_confirm.clicked.connect(self.ok)
        self.btn_cancel.clicked.connect(self.cancel)

        # object = QObject()

    def eventFilter(self, object, event):
        # eventFilter must put in the same thread with bond object
        # if not in the same thread, nothing will be done
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                # return True for stopping next operation
                # otherwise return False
                return True
                # if delete received object in eventFilter(), must return True
                # if return False, Qt will sender event to deleted object, which will lead to a crash
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or \
                        key.matches(QKeySequence.Paste):
                    return True
        # it is important to add this return, and it will return this event to QLineEdit object
        # keep sending this event to bond object
        return QDialog.eventFilter(self, object, event)

    def ok(self):
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, 'Warning', 'Empty password')
        elif len(self.text) < 6:
            QMessageBox.warning(self, 'Warning', 'Password length less than 6')
        else:
            # void QDialog::done(int r) Closes the dialog and sets its result code to r. If this dialog is shown with
            # exec(), done() causes the local event loop to finish, and exec() to return r.
            # end dialog by return 1 (self.exec_())
            self.done(1)

    def cancel(self):
        # end dialog by return 0 (self.exec_())
        self.done(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pd = PasswordDialog()
    pd.show()
    sys.exit(app.exec_())
