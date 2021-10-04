# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 21:55:22 2021

@author: gunen
"""

﻿import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True, type=str)
parser.add_argument("--country", required=True, type=str)
parser.add_argument("--petal-colour", required=True, choices=['R', 'W', 'Y', 'V', 'B'])
parser.add_argument("--stem-length", required=True, type=int)
parser.add_argument("--with-thorns", default=False, action='store_true')
parser.add_argument("--companion-plants", default=None, nargs='+')


with open("journal.txt", "a") as output_file:
    args = vars(parser.parse_args())
    json.dump(args, output_file)