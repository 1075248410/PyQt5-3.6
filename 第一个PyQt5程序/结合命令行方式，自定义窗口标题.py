# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
    app=QApplication(sys.argv)
    try:
        if len(sys.argv)<2:
            raise  ValueError
        else:
            title="".join(sys.argv[1:])
    except ValueError:
        title="学点编程"
    w=QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle(title)
    w.show()

    sys.exit(app.exec_())