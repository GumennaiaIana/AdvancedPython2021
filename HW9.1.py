# -*- coding: utf-8 -*-

def counter():
    num_sum = 0.0
    num_squares_sum = 0.0
    quantity = 0
    while True:
        number = yield
        quantity += 1
        num_sum += number
        num_squares_sum += number ** 2

        average = num_sum / quantity
        average_square = num_squares_sum / quantity
        print(f"Среднее: {average}, дисперсия: {average_square - average ** 2}, количество элементов: {quantity}")

coroutine = counter()
next(coroutine)
for number in range(7):
    coroutine.send(number)
    
    
    

