# -*- coding: utf-8 -*-

import json
import csv
import os
        
all_vitamins = []

for current_dir, dirs, files in os.walk("AdvancedPython2021"):
    with open('vitamins.json', 'w') as outfile:
        for name in files:
            if name.endswith(".txt"):
                with open (name, 'r') as file:
                    vitamin = {
                        "vitamin": file.readline().rstrip('\n'),
                        "vitamers": file.readline().rstrip('\n'),
                        "solubility": file.readline().rstrip('\n'),
                        "daily_requirement": file.readline().rstrip('\n'),
                        "deficiency_diseases": file.readline()
                        }
                    all_vitamins.append(vitamin)
        json.dump(all_vitamins, outfile)
    # получен файл vitamins.json
    
    with open("vitamin.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["vitamin", "vitamers", "solubility","daily_requirement", "deficiency_diseases"])
        for name in files:
            if name.endswith(".txt"):
                with open (name, 'r') as file:
                    writer.writerow([file.readline().rstrip('\n'), file.readline().rstrip('\n'),
                                          file.readline().rstrip('\n'), file.readline().rstrip('\n'),
                                          file.readline().rstrip('\n')])
    # получен файл vitamin.csv
                
    


