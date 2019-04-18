# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import  QApplication,QWidget
#QtWidgets模块包含了一整套UI元素组件，用于建立符合系统风格的classic界面，非常方便。
# 同时为了更方便的使用我们还明确了使用QtWidgets模块中的QApplication, QWidget
if __name__=='__main__':
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle("fcc出品")
    w.show()

    sys.exit(app.exec_())

'''
GUI应用程序都是事件驱动的。比如键盘事件、鼠标事件等等。
还有一些事件来自于系统内部，比如定时事件、其它文件事件等等。在没有任何事件的情况下，
应用程序处于睡眠状态。这种事件驱动机制，GUI应用程序都需要一个主循环(main loop)。
主循环(main loop)控制应用程序什么时候进入睡眠状态，什么时候被唤醒。
所以主循环(main loop)就是干这个的。

'''