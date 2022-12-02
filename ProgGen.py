# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:54:31 2022

@author: denis
"""
import sys
from Class.classGen import GenNum
from Class.classEvklid import Evklid
from Class.classEncryption import Encrypt

# Алгоритм Евклида для поиска НОД
def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2
#tytyty
# Генерируем два простых числа
p, q = 729109895220382741151, 66907724605396681871
p1 = GenNum(p)
p2 = p1.miller_rabin()
q1 = GenNum(q)    
q2 = q1.miller_rabin()

if p2 != True or q2 != True:
    sys.exit()
    
print("p = "+ str(p),", q = "+ str(q))

# Вычисляем модуль
n = p*q
print("n = " + str(n))

# Функция Эйлера
fi = (p-1)*(q-1)
print("fi = " + str(fi))

# Открытая экспонента 
# e = int(input("Введите e: "))
e = 9
print("Введите e: ", e)

# Взаимно простые ли числа? НОД должен быть == 1
# Должно быть простым
# Должно быть меньше fi 
a = gcd_rem_division(e, fi)
if a == 1:
    print("e и fi взаимно простые")
else:
    print("e и fi не взаимно простые")
    sys.exit()

# Теперь пара чисел e, n - открытый ключ. Отправляется для зашифровки

# d должно быть обратное е по модулю f. То есть остаток от деления по модулю f произведения dхe должен быть равен 1    
d1 = Evklid(e, fi)
d = d1.mulinv()
print("d = " + str(d))
# Пара d, n - закрытый ключ

# М должно быть меньше n 
M = 10011101000100001111
print("Сообщение для шифрования: "+ str(M))

# Шифрование
C = p1.Zpow(M, e, n)

print("Зашифрованное "+ str(C))

# Для расшифровки
# Решение методом китайских теорем об остатках
dp1 = Evklid(e, p-1)
dp = dp1.mulinv() # обратное значение е к р-1
dq1 = Evklid(e, q-1)
dq = dq1.mulinv() # обратное значение е к q-1
qlnv1 = Evklid(q, p)
qlnv = qlnv1.mulinv() # обратное значение q к p

# Разложение процесса расшифровки
m1 = p1.Zpow(C, dp, p)
m2 = p1.Zpow(C, dq, q)

h = (int(qlnv)*((int(m1) - int(m2))%p))%p
m = m2 + h*q

print("Расшифрованное " + str(m))












