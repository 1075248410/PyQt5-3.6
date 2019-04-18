# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QWidget,QApplication
from  PyQt5.QtGui import  QIcon



class ico(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry( 300, 300, 300, 220 )
        self.setWindowTitle( '学点编程吧出品' )
        self.setWindowIcon( QIcon( 'xdbcb8.ico' ) )
        self.show()


if __name__ == '__main__':
    app = QApplication( sys.argv )
    ex = ico()
    sys.exit( app.exec_() )