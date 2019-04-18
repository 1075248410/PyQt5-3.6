# -*- coding: UTF-8 -*-
from pynput import mouse,keyboard
from collections import deque
import threading,time,os,sys

#2019.1.11



class MouseClass(threading.Thread):
    def __init__(self, *args, **kwargs):
        super( MouseClass, self ).__init__( *args, **kwargs )
        self.mouse_listen = mouse.Listener()
        self.__mouse_run_flag_ = True  # 用于暂停鼠标线程不挂起
        self.__mouse_destroy_flag_ = True  # True鼠标监听不退出
        self.first_click_time=0.0


    def on_move(self,x,y):
        print( "Pointer moved to {0}  {1}".format( (x, y), time.ctime() ) )
        #false鼠标监听停止
        if not self.__mouse_destroy_flag_:
            return False

    def upate(self):
        j=time.time()
        print("update 函数{0}".format(j))
        k=j-self.first_click_time
        print(k)
        if self.first_click_time ==0.0:
            print("第一次")
        if(k>0.5) :
            print("大于0.5S")
            return False
        else:
            return True

    def on_click(self,x,y,button,pressed):


        if pressed:
            out='Pressed'
            gg = self.upate()
            self.first_click_time = time.time()
            if gg == True:
                print( "双机" )
            else:
                print( "单机" )
                self.first_click_time = time.time()
        else:
            out='Released'





        #print( '{0} at{1}'.format( 'Pressed' if pressed else 'Released', (x, y) ) )
        #print( '{0} at{1}'.format( out, (x, y) ) )
        # false鼠标监听停
        if (not self.__mouse_destroy_flag_) or (not pressed):
            return False


    def run(self):

        while 1:

            with mouse.Listener( no_move = self.on_move, on_click = self.on_click,suppress= not self.__mouse_run_flag_) as self.mouse_listen:
                self.mouse_listen.join()
                if not self.__mouse_destroy_flag_:
                    break

def mouse_test():

    km = MouseClass()

    print( '1.Start runing...' )

    km.start()




mouse_test()
