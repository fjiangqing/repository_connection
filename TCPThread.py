#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import _thread
import time

import sys
import RPi.GPIO as GPIO
import time
import signal
import atexit

# 导入 socket、sys 模块
import socket
import sys

# =============================================================================
# #设定光敏传感器 
# lightPin = 7   较亮
# #土壤检测传感器
# turan = 13
# #继电器检测
# relay = 15
# #设定舵机控制
# servopin = 40
# =============================================================================

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
#host = socket.gethostname()
host = "127.0.0.1"
# 设置端口好
port = 9500

# 连接服务，指定主机和端口
# s.connect((host, port))


#设定GPIO 使用板物理引脚模式
GPIO.setmode(GPIO.BOARD)

#设定光敏传感器 
lightPin = 7

#设定引脚输入模式
GPIO.setup(lightPin, GPIO.IN)
time.sleep(0.5)

#土壤检测传感器
turan = 13
GPIO.setup(turan, GPIO.IN)
time.sleep(0.5)

#继电器检测
relay = 15
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)

#设定舵机控制
servopin = 40
GPIO.setup(servopin, GPIO.OUT, initial=False)
#设定频率50HZ  
p = GPIO.PWM(servopin, 50)
p.start(0)
time.sleep(2)
JD = 0


# msg = "test"
# # 为线程定义一个函数
# def print_time():
#     # 创建 socket 对象
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 获取本地主机名
#     #host = socket.gethostname()
#     host = '192.168.56.1'
#     # 设置端口好
#     port = 9500
#     # 连接服务，指定主机和端口
#     s.connect((host, port))
    
#     while 1:
#         #s.send(msg.encode('utf-8'))
#         global msg
#         msg = s.recv(1024)
#         #time.sleep(4)
#         #print (msg)
#         #sysPZ()
#         # JSON 解析
#         #
#         #data2 = json.loads(msg)
#         #print(data2['uploadingName'])
        
#     s.close()

# def myprint():
#     while 1:
#         print(msg)
#         time.sleep(5)
# # 创建两个线程
# try:
#     print('run')
#     _thread.start_new_thread(print_time,())
#     _thread.start_new_thread(myprint, () )

# except:
#     print ("Error: unable to start thread")

ZD = 0
JS = 1

GS_cnt = 0
while(True):
    
    #检测土壤湿度
    t = GPIO.input(turan)
    if ((t == GPIO.LOW and ZD == 0)  or  (ZD == 1 and JS == 1)):
        GPIO.output(relay, GPIO.LOW)
        time.sleep(0.1)
        
        ## turang = 1 浇水信号
        msg = '{"turang": "1"}'
        #s.send(msg.encode('utf-8'))
        # s.send(msg.encode('utf-8'))
        # s.close()
        print (msg.encode('utf-8'))
        
    if(t == GPIO.HIGH):
        GPIO.output(relay, GPIO.HIGH)
        time.sleep(0.01)
        
        ## turang = 0 不浇水信号
        msg = '{"turang": "0"}'
        #s.send(msg.encode('utf-8'))
        # s.send(msg.encode('utf-8'))
        # s.close()
        print (msg.encode('utf-8'))
        
    v = GPIO.input(lightPin)
    if (v == GPIO.HIGH and JD != 80):
        #打开光栅
        if(GS_cnt < 100):
            GS_cnt = GS_cnt + 1
        else:
            JD = 80  
            for i in range(30,80,1):
                p.ChangeDutyCycle(2.5 + 10 * i/180)
                time.sleep(0.02)
                p.ChangeDutyCycle(0)
                time.sleep(0.02)
                print ('out 7 LOW')
         

    if ( v == GPIO.LOW and JD != 30):

        if(GS_cnt > 0):
            GS_cnt = GS_cnt - 1
        
        else:
            #关闭光栅
            JD = 30
            for i in range(80,25,-1):
                p.ChangeDutyCycle(2.5 + 10 * i/180)
                time.sleep(0.02)
                p.ChangeDutyCycle(0)
                time.sleep(0.02)
                print ('out 7 HIGH')
            
        
