# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:04:21 2019

@author: NATSUKI
"""

code=str(input("暗号文(アルファベット）> "))
code_list=list(code)
abc=[chr(i) for i in range(97, 97+26)]#a,b,c---z
ABC=[chr(i) for i in range(65, 65+26)]#A,B,C---Z
count=[0 for i in range(26)]
#暗号文の中でa(0),b(1),c(2)が何回つかわれたか
count_dic={}
key=0
option=["e",	"a",	"t",	"i",	"o",	"s",	"n",	"r",	"h",	"l",	"d",	"c",	"u",	"m",	"p",	"f",	"g",	"y",	"w",	"b",	"v",	"k",	"j",	"x",	"q",	"z"]
anser=True
zyx=[]

for i in range(len(code_list)):
    if code_list[i].lower() in abc:
        count[abc.index(code_list[i].lower())]+=1


s=0
count_max=max(count)#countの最大値
while anser:
    plian_list=[]
    key=abs(abc.index(option[s])-count.index(count_max))
    zyx=abc[key:]+abc[0:key]

    for i in range(len(code)):
        if code[i] in abc:
            index_num=zyx.index(code[i])
            plian_list.append(abc[index_num])
        elif code[i] in ABC:
            index_num=zyx.index(code[i].lower())#ここでのcodeは大文字なので小文字にする
            plian_list.append(ABC[index_num])
        else:
            plian_list.append(code[i])

    print("\n平文候補＞　"+"".join(plian_list))
    yn=str(input("\n意味のある文字列？（y/n）＞ "))
    if yn=="n":
        anser=True
    else:
        anser=False

    s+=1

print("解読終了")
