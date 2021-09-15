# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 00:18:08 2021

@author: gunen
"""

words = []
alph = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
while True:
    a = input()
    if a != "End":
        if a != "-1":
            words.append(alph[int(a)])
        else:
            words.append(" ")
    else:
        break
for k in range(len(words)):
    print(words[k], end='')

    