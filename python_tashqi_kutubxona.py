# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 14:33:16 2025

@author: acer
"""

# from googletrans import Translator 

# matn_uz="Payton dunyodagi eng mashhur dasturlash tili"
# tarjimon=Translator()

# tarjima=tarjimon.translate(matn_uz, dest='en')
# print(tarjima.origin)
# print(tarjima.text)

from deep_translator import GoogleTranslator as gt

# matn="Tarjima uchun so'z kiriting.(chiqib ketish uchun \"q\" ni kiriting): "
# while True:
#     text=input(matn)
#     if text=="q":
#         break
#     else:
#         tarjima=gt(source='auto', target='uz').translate(text)
#         print(tarjima)
import requests
# from pprint import pprint
# # sahifa="https://kun.uz/news/main"
# # r=requests.get(sahifa)
# # pprint(r.text)
# country="USA"
# url=f"https://restcountries.com/v3.1/name/{country}"
# r=requests.get(url)
# r_json=r.json()[0]
# print("Poytaxt:", r_json["capital"][0])

url="https://api.adviceslip.com/advice"
r=requests.get(url)
advice=r.json()['slip']['advice']
print(advice)
translator=deep_translator.gt()
tarjima=translator.
    
    

