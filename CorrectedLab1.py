# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 00:18:08 2021

@author: gunen
"""

words = []
alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]
sequence = input()
while sequence != "End":
    words.append(alphabet[int(sequence)])
    sequence = input()
print(''.join(words))
