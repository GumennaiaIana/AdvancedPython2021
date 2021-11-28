# -*- coding: utf-8 -*-

import re

s = '''def print_hello(): 
print("Hello!")
class Goodbyer:
def print_goodbye(self):
print('Bye!')'''

print(re.findall("(?=def).+\s+.+.+", s))