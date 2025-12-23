# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 15:52:18 2025

@author: acer
"""

def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'korobka':korobka,
          'yil':yili,
          'narh':narhi}
    return avto
print("Saytimizdagi avtolar ro'yxatini to'liq shakllantiramiz")
def avto_kirit():
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting:", end='')
    kompaniya=input("Ishlab chiqaruvchi:")
    model=input("Modeli:")
    rang=input("Rangi:")
    korobkasi=input("Korobka:")
    yili=input("Ishlab chiqarilgan yili:")
    narh=input("Narhi:")
    
    avtolar.append(avto_info(kompaniya,model,rang,korobkasi,yili,narh))
    
    javob=input("Yana avto qo'shasizmi (ha/yo'q):")
    if javob=="yo'q":
        break
return avtolar
def info_print(avto_info)
print("\nSalonimizdagi avtolar:")

    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka'].upper()} korobka "
          f"{avto_info['yil']}-yil,{avto_info['narh']}$"
    
    

