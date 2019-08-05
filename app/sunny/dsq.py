#encoding:utf-8
#引入库 threading
import threading
#定义函数
def fun_timer():
    print('hello timer')   #打印输出
    global timer  #定义变量
    timer = threading.Timer(60,fun_timer)   #60秒调用一次函数
    #定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
    timer.start()    #启用定时器
timer = threading.Timer(1,fun_timer)  #首次启动
timer.start()