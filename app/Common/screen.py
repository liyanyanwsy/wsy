import os
import time
# def screenshot():
   #  #PATH = lambda p: os.path.abspath(p)
   # # path = PATH(os.getcwd() + "/screenshot")
   #  timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
   #  print timestamp
   #  os.popen("adb wait-for-device")
   #  #os.popen("adb shell screencap -p /sdcard/data/local/tmp/tmp.png")
   #  os.popen("adb shell screencap -p /sdcard/screenshot/tmp.png")
   #  #if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
   #      #os.makedirs(path)
   #  #os.popen("adb pull /sdcard/data/local/tmp/tmp.png D:/download/12.png")
   #  #os.popen("adb pull /sdcard/data/local/tmp/tmp.png PATH(path + '/' + timestamp + '.png')" )
   #  #temp='D:/download/' +timestamp + '.png'
   #  temp='D:/appscreenshot/' +timestamp + '.png'
   #  os.popen("adb pull /sdcard/screenshot/tmp.png " + temp )
   #  os.popen("adb shell rm /sdcard/screenshot/tmp.png")
   # # print timestamp
   #  #print "success"

def screenshot():
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /sdcard/screenshot/tmp.png")
    temp='D:/appscreenshot/' +timestamp + '.png'
    os.popen("adb pull /sdcard/screenshot/tmp.png " + temp )
    os.popen("adb shell rm /sdcard/screenshot/tmp.png")
screenshot()
# if __name__ == "__main__":
#     screenshot()

#
# def screenshot001():
#     timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
#     os.popen("adb wait-for-device")
#     os.popen("adb shell screencap -p /sdcard/screenshot/tmp.png")
#     temp='D:/appscreenshot/' +timestamp + '.png'
#     os.popen("adb pull /sdcard/screenshot/tmp.png " + temp )
#     os.popen("adb shell rm /sdcard/screenshot/tmp.png")
# screenshot001()