# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:31:04 2018
负责接收云端的命令进行拍照，拍照完成后调用将文件名称上传给上传程序
@author: fjiangqing
"""

# 导入 socket、sys 模块
import socket
import sys
import json
import time
#import os  

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
# host = "192.168.137.1"
# 设置端口好
port = 9500
# port = 8080

# 连接服务，指定主机和端口
s.connect((host, port))

# msg = '{"abc": "123"}'
# s.send(msg.encode())



def sysPZ():
    # 直接使用os.system调用一个echo命令  
    # 当前最新图片文件约定，now.jpg
    #os.system("raspistill -w 600 -h 400 -t 100 -o now.jpg")
    print("hello PYTHON")
    msg = '{"uploadingName": "get-123.PNG"}'
    s.send(msg.encode('utf-8'))
    #添加链接到中转发送图片代码

print('拍照程序运行')
while 1:
    # msg = s.recv(1024)
    # text = json.loads(msg)
    # try:
    #      if(text['PZ'] == 1):
    #         sysPZ()
    # except json.decoder.JSONDecodeError:
    #     print("err")
    
    sysPZ()
    #延时5s
    time.sleep(5)
    