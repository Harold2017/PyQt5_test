import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QPushButton
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Learn PyQt5')

        btn_scissor = QPushButton('Scissor', self)
        btn_scissor.setGeometry(30, 180, 50, 50)

        btn_rock = QPushButton('Rock', self)
        btn_rock.setGeometry(100, 180, 50, 50)

        btn_cloth = QPushButton('Cloth', self)
        btn_cloth.setGeometry(170, 180, 50, 50)

        # bind all clicked signals to buttonclicked function
        btn_scissor.clicked.connect(self.buttonclicked)
        btn_rock.clicked.connect(self.buttonclicked)
        btn_cloth.clicked.connect(self.buttonclicked)

        self.show()

    def buttonclicked(self):
        computer = randint(1, 3)
        player = 0
        # sender() indicate the signal origin
        sender = self.sender()
        sender_player = {'Scissor': 1,
                         'Rock': 2,
                         'Cloth': 3}
        player_sender = {1: 'Scissor',
                         2: 'Rock',
                         3: 'Cloth'}
        player = sender_player.get(sender.text())
        result = player - computer
        result_alert = {0: 'Draw',
                        1: 'Player Win',
                        -1: 'Computer Win',
                        -2: 'Player Win',
                        2: 'Computer Win'}
        out = 'Player: {0}, Computer: {1}\n'.format(player_sender.get(player), player_sender.get(computer))\
              + result_alert.get(result)
        QMessageBox.about(self, 'Result', out)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
