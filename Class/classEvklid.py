# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:20:15 2022

@author: denis
"""


class Evklid():
    
    def __init__(self, b, n):
        self.b = b
        self.n = n
        print("Шифровка/Расшифровка")
    
    # нахождение обратного элемента в кольце по модулю
    # Расширенный алгоритм Евклида
    # Протектед метод
    def _egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = Evklid._egcd(b % a, a)
            return (g, y - (b // a) * x, x)
     
    def mulinv(self):
        g, x, _ = Evklid._egcd(self.b, self.n)
        # если остаток равен 1
        if g == 1:
            return x % self.n