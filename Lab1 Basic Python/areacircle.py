# -*- coding: utf-8 -*-
"""AreaCircle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1brnkcIfVwWxGUDG36v_aA-azicc6qIe5
"""

"""
เขียนโปรแกรม Python ซึ่งรับ input เป็นรัศมีของวงกลม จากนั้นคำนวณพื้นที่และแสดงผล
"""

import math
r = float(input('r='))
pi_r  = math.pi
x = r*r*pi_r
a= str(x)
print("Area="+a)