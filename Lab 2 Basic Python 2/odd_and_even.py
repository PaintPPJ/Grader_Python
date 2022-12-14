# -*- coding: utf-8 -*-
"""Odd And Even.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BZvdaUfZ2JcGMP9tvtGjO5Ybf_DSbOTn
"""

"""
ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการหาตำแหน่ง คู่ กับ คี่ จาก List และ String

def odd_even(type, data, mode):
    //Code Here

โดยที่รูปแบบการรับ Input ตำแหน่งแรกจะเป็นตัวบอกว่าเป็น String หรือ List ถ้าใส่ S = String ถ้าใส่ L = List

Input ตำแหน่งที่สองเป็นค่าใน String หรือ List ที่นำเข้ามา

Input ตำแหน่งที่สามเป็นการบอกว่าจะแสดงตำแหน่งคู่หรือคี่ ถ้าใส่ Odd = คี่ ถ้าใส่ Even = คู่
"""

def odd_even(data,pos):
  listAns = []
  if pos == 'Odd' :
    for i in range(0,len(data)):
      if i % 2 == 0:
        listAns.append(data[i])
  if pos == 'Even' :
    for i in range(0,len(data)):
      if i % 2 == 1:
        listAns.append(data[i])
  return listAns

print("*** Odd Even ***")
type_ , data , pos = input('Enter Input : ').split(',') #type คือ S หรือ L , pos คือ Odd หือ Even
thisList = []
data = str(data) #casting หรือ แปลง data ให้เป็น  datatype 'string'
if type_ == 'S':
  for i in range(0,len(data)): #ใส่เป็น string เช่น ACE
    thisList.append(data[i])
if type_ == 'L':
  thisList = data.split('') #ใส่เป็น List เช่น ['2', '4']
listAns = odd_even(thisList,pos) #เรียก Function odd_even ประกาศตัวแปร listAns
if type_ == 'S':
  for i in range(0,len(listAns)):
    print(listAns[i],end='') #loop for print ทีละตัว ปล. string ต้องใช้ loop เพื่อ print Array  >>>>>>> Source : https://www.w3schools.com/python/python_strings.asp 
if type_ == 'L' :
  print(listAns) #https://www.w3schools.com/python/python_lists.asp



