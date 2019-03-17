# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:31:04 2018

@author: fjiangqing
"""

import os  

def sysPZ():
    # 直接使用os.system调用一个echo命令  
    os.system("raspistill -w 600 -h 400 -t 100 -o P1.jpg")
    
#sysPZ()