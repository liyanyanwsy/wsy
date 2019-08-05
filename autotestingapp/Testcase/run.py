# encoding:utf-8
import unittest
import time, os
from selenium import webdriver
import sys

def setup(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 设备系统
    desired_caps['platformVersion'] = '5.1'  # 设备系统版本
    desired_caps['deviceName'] = 'Y55DJZ9D99999999'  #  设备名称
    desired_caps['appPackage'] = 'com.igen.solarmanpro'
    desired_caps['appActivity'] = 'com.igen.solarmanpro.activity.MainActivity'
    self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
def teardown(self):
    self.driver.quit()

PATH = lambda p: os.path.abspath(p)

def screenshot():
    path = PATH(os.getcwd() + "/screenshot")
    now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
        os.makedirs(path)
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + now + ".png"))
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    print "success"

if __name__ == "__main__":
    screenshot()


