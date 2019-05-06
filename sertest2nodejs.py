 # -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:36:09 2018

@author: fjiangqing
"""

# 导入 socket、sys 模块
import socket
import sys
import json
#import PZ


# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
#host = socket.gethostname()
# ============================ =================================================
# host = '192.168.56.1'
# =============================================================================

# 设置端口好
port = 9500
 
# 连接服务，指定主机和端口
s.connect((host, port))
 
# 接收小于 1024 字节的数据
#msg = s.recv(1024)

msg = '{"uploadingName": "get-123.png"}'
msg = msg.encode('utf-8')
count = 0
while 1:
    #s.send(msg.encode('utf-8'))
    
    
    s.send(msg)
    msg = s.recv(1024)
    print (msg)
    #sysPZ()
    # JSON 解析
    #
    #data2 = json.loads(msg)
    #print(data2['uploadingName'])
    
s.close()