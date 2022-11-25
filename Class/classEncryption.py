# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:31:55 2022

@author: denis
"""


class Encrypt():
    def __init__(self, n):
        self.n = n
        print("Запуск генерации простых чисел")
    
    # возведение в степень по модулю в кольце
    def Zpow(self, a, p, m):
        result = 1
        while p > 2: # когда степень сократится до квадрата и меньше - завершаем
            if p % 2 == 0: # если степень кратна 2
                a = (a ** 2) % m # понижаем степень, возводя число в квадрат
                p = p // 2
            else:
                # выносим множитель для четной степени
                result = (result * a) % m
                p = p - 1
        a = (a ** p) % m
        result = (result * a) % m
        return result
    