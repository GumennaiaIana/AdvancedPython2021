# -*- coding: utf-8 -*-

#Обычное условие

from typing import List, Optional
import random

class RandomChoiceIterator:
    def __init__(self, values: List[int], num_iters: Optional[int] = None):
        self.values = values
        self.num_iters = num_iters
        self.current_iter = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num_iters is None:
            while True:
                return random.choice(self.values)
        else:
            while self.num_iters > self.current_iter:
                self.current_iter += 1
                return random.choice(self.values)
            raise StopIteration()
            
for value in RandomChoiceIterator([1, 2, 3], num_iters=5):
    print(value)