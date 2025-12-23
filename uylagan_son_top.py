# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 14:04:54 2025

@author: acer
"""
import random
def son_top(x):
    """Kampyuter o'ylagan sonni topish funksiyasi"""
    uylangan_son=random.randint(1, x)
    taxmin=0
    print(f"1 dan {x} gacha son o'yladim topa olasizmi:")
    while True:
        savol=int(input('>>>'))
        taxmin+=1
        if uylangan_son>savol:
            print("Xato men o'ylgan son bundan kattaroq yana harakat qiling iltimos: ")
        elif uylangan_son<savol:
            print("Xato men o'ylgan son bundan kichikroq yana harakat qiling: ")
        else:
             break 
    print(f"Topdingiz men {uylangan_son} o'ylagan edim. Siz {taxmin} ta taxmin bilan topdingiz tabriklayman!!")         
    return taxmin       


def son_top_ks(x):
    """Men o'ylagan sonni kompyuter topadi"""
    sana=0
    yuqori=x
    quyi=1
    input(f"1 dan {x} gacha son o'ylang men topishga harakat qilaman.\nSon o'ylagan bo'lsangiz istalgan tugmani bosing: ")
    
    
    while True:
        if quyi!=yuqori: 
            taxmin=random.randint(quyi, yuqori)
        else:
            taxmin=quyi
        javob=input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t), men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)???")
        sana+=1
        if javob=='-':
            yuqori=taxmin-1
        elif javob=='+':
            quyi=taxmin+1
        else:
            break
    
    print(f"Soningizni {sana} ta taxmin bilan topdim. URAAAA")   
    return sana


def play(x):
    yana=True
    while yana:
        foydalanuvchi=son_top(x)
        kompyuter=son_top_ks(x)
        if foydalanuvchi>kompyuter:
            print(F" Sizni {kompyuter} ta taxmin bilan yutdim.")
        elif foydalanuvchi<kompyuter:
            print(f" Siz meni yutdingiz.")
        else:
            print(f"DURRANG. IKKIMIZ HAM {foydalanuvchi} ta taxmin bilan G'OLIBMIZ.")
        yana=int(input("Yana o'ynaymizmi ha(1), yo'q(0): "))
print(play(25))
            
    
        
    


      
        
        