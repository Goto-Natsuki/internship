# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:31:03 2019

@author: NATSUKI
"""

plian=str(input("平文(アルファベット）> "))
key=int(input("ずらす文字数 > "))
abc=[chr(i) for i in range(97, 97+26)]#a,b,c---z
ABC=[chr(i) for i in range(65, 65+26)]#A,B,C---Z
zyx=abc[key:]+abc[0:key]
plian_list=list(plian)
code_list=[]
index_num=0
code=""

for i in range(len(plian_list)):
    if plian_list[i] in abc:
        index_num=abc.index(plian_list[i])
        code_list.append(zyx[index_num])
    elif plian_list[i] in ABC:
        index_num=ABC.index(plian_list[i])
        code_list.append(zyx[index_num].upper())#zyxは小文字なので
    else:
        code_list.append(plian_list[i])

code="".join(code_list)
print("\n暗号文　＞"+code)
