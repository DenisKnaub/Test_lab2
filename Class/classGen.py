import random
import sys
from Class.classEncryption import Encrypt

class GenNum(Encrypt):

    # тест Рабина-Миллера на простоту
    def miller_rabin(self):
        k = 40
        if self.n == 3 or self.n == 2:
            print(self.n, "простое число")
            return True
        if self.n % 2 == 0:
            print(self.n, "непростое число")
            return False
            
            
        # представим n − 1 в виде (2^s)·t, где t нечётно, 
        # это можно сделать последовательным делением n - 1 на 2
        s, t = 0, self.n - 1
        while t % 2 == 0:
            s += 1 # степень двойки при делении на 2
            t //= 2 # должны получить нечетное t

        for _ in range(k):
            # генерация случайного целого числа в отрезке [2, n-1]
            a = random.randrange(2, self.n - 1)

            # x ← a^t mod n (с помощью возведения в степень по модулю)
            x = self.Zpow(a, t, self.n)
            if x == 1 or x == self.n - 1:
                continue

            for _ in range(s - 1):
                # x ← x^2 mod n
                x = self.Zpow(x, 2, self.n)

                # если x == n − 1, то перейти на следующую итерацию внешнего цикла
                if x == self.n - 1:
                    break
            else:
                print(self.n, "непростое число")
                return False
        print(self.n, "простое число")
        return True

    # # генерация чисел
    # def gen():
    #     y = False
    #     while y != True:  # цикл для генерации простых чисел 
    #         a = random.randint(1000000000000000, 1000000000000000000000) # диапазон генерации чисел
    #         y = miller_rabin(a, 40)
    #         if y == True:
    #             return a
         