# -*- coding: utf-8 -*-
"""Spherical.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gEguhPJMg4jrPqF1JxYNzyj3MmyjBfUs
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
สร้าง class Spherical โดยต้อง

มี function [changeR , findVolume , findArea]

มี ตัวแปร radius



*สามารถใช้ from math import pi  หรือ math.pi  ได้*

class Spherical:

    def __init__(self,r):

        ### Enter Your Code Here ###

    def changeR(self,Radius):

        ### Enter Your Code Here ###

    def findVolume(self):

        ### Enter Your Code Here ###

    def findArea(self):

        ### Enter Your Code Here ###

    def __str__(self):

        ### Enter Your Code Here ###

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Spherical

from math import pi
class Spherical:

    def __init__(self,r):
      self.radius = r

    def changeR(self,Radius):
      self.radius = Radius

    def findVolume(self):
      return 4/3 * pi * (self.radius*self.radius*self.radius)

    def findArea(self):
      return 4 *pi * (self.radius*self.radius)
    def __str__(self):
      return 'Radius =' + str(self.radius) + ' Volumn = ' + str(self.findVolume()) + ' Area = ' + str(self.findArea())
  
input1,input2 = input('Enter R : ').split()
R1 = Spherical(int(input1))
print(type(R1))
print(dir(R1)) #Python dir() >>>>> In this tutorial, you will learn about the Python dir() method with the help of examples. >>>>>> https://www.programiz.com/python-programming/methods/built-in/dir >>>>>>> https://www.w3schools.com/python/trypython.asp?filename=demo_ref_dir
R1.changeR(int(input2))
print(R1)