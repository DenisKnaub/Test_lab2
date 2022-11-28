# Test_lab2
[![code checks](https://github.com/DenisKnaub/Test_lab2/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/DenisKnaub/Test_lab2/actions/workflows/checks.yml)
[![Coverage Status](https://coveralls.io/repos/github/DenisKnaub/Test_lab2/badge.svg?branch=main)](https://coveralls.io/github/DenisKnaub/Test_lab2?branch=main)

#Тестирование приложения "Шифрование/Расшифровывание" с помощью библиотеки pytest

__Pytest__ - это платформа тестирования программного обеспечения, основанная на языке программирования Python. Он может быть использован для написания различных типов тестов программного обеспечения, включая модульные тесты, интеграционные тесты, сквозные тесты и функциональные тесты.

##Было реализовано 14 тестов:
___Тест 1-4.___
```python
@pytest.mark.parametrize("number, result", [(10, False),
                                                 (3, True),
                                                 (729109895220382741151, True),
                                                 (895220382741150, False)])
# тест проверяет число на простоту
def test_check(number, result):
    p1 = GenNum(number)
    assert p1.miller_rabin() == result
```
Тест создает обьект и вызывает функцию __miller_rabin()__ и проверяет коректность работы алгоритма на поиск простого или непростого числа

```python
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
```
___Тест 5.___
```python
def test_check_error():
    with pytest.raises(TypeError):
         p1 = GenNum("f")
         p1.miller_rabin()

```
Тест создает обьект и вызывает функцию __miller_rabin()__ и проверяет функцию на корректность ввода чисел

```python
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
```

___Тест 6-8.___
```python
@pytest.mark.parametrize("C, dp, p, result", [(7, 4, 13, 9),
                                                 (5, 18, 23, 6),
                                                 (555, 189534859834, 23345435435, 15540107060)])
# тест проверяет работу возведение в степень по модулю в кольце
def test_Zpow(C, dp, p, result):
    p1 = GenNum(7)
    assert p1.Zpow(C, dp, p) == result

```
Тест создает обьект и вызывает функцию __Zpow()__ и проверяет корректную работу возведения в степень по модулю в кольце

```python
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
```

___Тест 9-11.___
```python
@pytest.mark.parametrize("C, dp, p, result", [("f", 4, 13, TypeError),
                                                  (5, "f", 23, TypeError),
                                                  (555, 189534859834, "f", TypeError)])
# отрицательный тест проверяет работу возведение в степень по модулю в кольце
def test_Zpow_error(C, dp, p, result):
    with pytest.raises(result):
        p1 = GenNum(7)
        p1.Zpow(C, dp, p) 

```
Тест создает обьект и вызывает функцию __Zpow()__ и проверяет функцию на корректность ввода чисел

```python
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
```

___Тест 12-14.___
```python
@pytest.mark.parametrize("e, qp, result", [(7, 729109895220382741150, 624951338760328063843),
                                                  (7, 66907724605396681870, 19116492744399051963),
                                                  (729109895220382741151, 66907724605396681871, 33906931489378411384)
                                                ])
# тест проверяет нахождение обратного элемента в кольце по модулю
# Расширенный алгоритм Евклида
def test_evklid(e, qp, result):
    dp1 = Evklid(e, qp)
    assert dp1.mulinv() == result # обратное значение е к р-1

```
Интеграционный тест создает обьект и вызывает функцию __mulinv()__ и проверяет нахождение обратного элемента в кольце по модулю расширенным алгоритмом Евклида

```python
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
```

