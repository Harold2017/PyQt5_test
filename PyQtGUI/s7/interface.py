import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # status bar
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Learn PyQt5')

        # QAction is Object for using menuBar / toolBar / user-defined keyboard shortcut
        # create exit action and connect it to qApp
        # add & to use alt+E as keyboard shortcut
        exitAct = QAction(QIcon('exit.png'), 'Exit(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit program')
        exitAct.triggered.connect(qApp.quit)

        # create new menu object with QMenu
        saveMenu = QMenu('Save(&S)', self)
        saveAct = QAction(QIcon('save.png'), 'Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save file')
        saveasAct = QAction(QIcon('saveas.png'), 'Save as(&O)', self)
        saveasAct.setStatusTip('File save as')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction(QIcon('new.png'), 'New(&N)', self)
        newAct.setShortcut('Ctrl+N')

        # create menubar and add menu to it
        # add action to menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)

        # add separator between menus
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        # toolbar
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)

        self.show()

    # redefine contextMenuEvent() method
    def contextMenuEvent(self, e):
        cmenu = QMenu(self)

        newAct = cmenu.addAction('New')
        saveAct = cmenu.addAction('Save')
        quitAct = cmenu.addAction('Exit')
        # apply exec_() method to show context menu
        # and obtain mouse position from event object
        # mapToGlobal() method will transfer widget coordinate to global screen coordinate
        action = cmenu.exec_(self.mapToGlobal(e.pos()))
        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
