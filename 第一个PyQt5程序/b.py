from pynput import mouse, keyboard
from collections import deque
import threading, time, os, sys

'''

1.说明：

    1.0.tcy shanghai 2018/8/28 测试平台windows7 python3.7 pycharm20182.1

    1.1. 一个鼠标监听器是一个线程。所有的回调将从线程调用。

    1.2. 任何地方调用pynput.mouse.Listener.stop，mouse.Listener.StopException

          或从回调中返回False来停止监听器。

2.用途：

    1.1.本函数主要用作鼠标监听

    1.2.实现鼠标监听暂停启动停止；停止和销毁后不能再进行鼠标监听，暂停后可 

3.技术要点

    1.1.采用鼠标监听内部的线程挂起，当暂停时鼠标不起左右，恢复后又正常工作。

'''


class MouseClass( threading.Thread ):
    def __init__(self, *args, **kwargs):
        super( MouseClass, self ).__init__( *args, **kwargs )
        self.mouse_listion = mouse.Listener()
        self.__mouse_run_flag_ = True# 用于暂停鼠标线程不挂起

        self.__mouse_destroy_flag_ = True# True鼠标监听不退出

    def on_move(self, x, y):

        print( "Pointer moved to {0}  {1}".format( (x, y), time.ctime() ) )

        if not self.__mouse_destroy_flag_:# false鼠标监听停止
            return False

    def on_click(self, x, y, button, pressed):
        print( '{0} at{1}'.format( 'Pressed' if pressed else 'Released', (x, y) ) )
         # 凸轮键松开鼠标监控停止

        if (not self.__mouse_destroy_flag_) or (not pressed):  # false鼠标监听停
            return False

    def on_scroll(self, x, y, dx, dy):

        print( 'Scrolled {0} at {1}'.format( 'down' if dy < 0 else 'up', (x, y) ) )
        if not self.__mouse_destroy_flag_: # false鼠标监听停止
            return False

    def run(self):

        while 1:

            with mouse.Listener( no_move = self.on_move, on_click = self.on_click,suppress= not self.__mouse_run_flag_) as self.mouse_listion:
                self.mouse_listion.join()
                if not self.__mouse_destroy_flag_:
                    break

    def mouse_pause(self):

        self.__mouse_run_flag_ = False
        print( '鼠标暂停...;当前线程==>%s ;线程数量==%d\n' % (
        threading.current_thread().name, threading.activeCount() ))


    def mouse_resume(self):

        self.__mouse_run_flag_ = True

        print( '鼠标恢复...;当前线程==>%s ;线程数量==%d\n' % (threading.current_thread().name, threading.activeCount() ))

    def mouse_destroy(self):

        self.__mouse_destroy_flag_ = False# 鼠标监听停止
        self.__mouse_run_flag_ = True
        print( '鼠标监听停止;当前线程==>%s ;线程数量==%d\n' % (threading.current_thread().name, threading.activeCount() ))

# 测试函数

def mouse_test():

    km = MouseClass()

    print( '1.Start runing...' )

    km.start()




mouse_test()

# 输出结果：

# 1.Start runing...

# Pressed at (321, 553)

# Released at (321, 553)

# Scrolled down at (321, 553)

# Scrolled down at (320, 556)

# Scrolled down at (320, 556)

# 2.Mouse pause...

# 鼠标暂停...;当前线程==>MainThread ;线程数量==3

'''此时鼠标不起作用'''

# Scrolled down at (320, 556)

# Scrolled down at (320, 556)

# Pressed at (320, 556)

# Released at (320, 556)

# Scrolled down at (320, 556)

# Scrolled down at (320, 556)

'''估计是将队列中的剩余任务输出；参考原函数定义'''

# 3.Mouse start....

# 鼠标恢复...;当前线程==>MainThread ;线程数量==3

'''此时鼠标起作用'''

# Pressed at (320, 556)

# Released at (320, 556)

# Scrolled down at (320, 556)

# 4.Mouse stop....

# 鼠标监听停止;当前线程==>MainThread ;线程数量==3

# Scrolled down at (320, 556)

'''将队列中的剩余任务输出；鼠标监听退出，等待主线程完成'''

# 5.End all program!

# 当前线程==>MainThread ;线程数量==1



