# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:08:17 2022

@author: denis
"""

import pytest
from Class.classGen import GenNum
from Class.classEvklid import Evklid

# Модульный тест!
@pytest.mark.parametrize("number, result", [(10, False),
                                                 (3, True),
                                                 (729109895220382741151, True),
                                                 (895220382741150, False)])
# тест проверяет число на простоту
def test_check(number, result):
    p1 = GenNum(number)
    assert p1.miller_rabin() == result

# отрицательный тест на ввод букв
def test_check_error():
    with pytest.raises(TypeError):
         p1 = GenNum("f")
         p1.miller_rabin()

# Модульный тест!
@pytest.mark.parametrize("C, dp, p, result", [(7, 4, 13, 9),
                                                 (5, 18, 23, 6),
                                                 (555, 189534859834, 23345435435, 15540107060)])
# тест проверяет работу возведение в степень по модулю в кольце
def test_Zpow(C, dp, p, result):
    p1 = GenNum(7)
    assert p1.Zpow(C, dp, p) == result

@pytest.mark.parametrize("C, dp, p, result", [("f", 4, 13, TypeError),
                                                  (5, "f", 23, TypeError),
                                                  (555, 189534859834, "f", TypeError)])
# отрицательный тест проверяет работу возведение в степень по модулю в кольце
def test_Zpow_error(C, dp, p, result):
    with pytest.raises(result):
        p1 = GenNum(7)
        p1.Zpow(C, dp, p) 

# Интеграционный тест
@pytest.mark.parametrize("e, qp, result", [(7, 729109895220382741150, 624951338760328063843),
                                                  (7, 66907724605396681870, 19116492744399051963),
                                                  (729109895220382741151, 66907724605396681871, 33906931489378411384)
                                                ])
# тест проверяет нахождение обратного элемента в кольце по модулю
# Расширенный алгоритм Евклида
def test_evklid(e, qp, result):
    dp1 = Evklid(e, qp)
    assert dp1.mulinv() == result # обратное значение е к р-1
    
if __name__ == '__main__':
    pytest.main()