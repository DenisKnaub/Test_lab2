# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:08:17 2022

@author: denis
"""

import pytest
from Class.classGen import GenNum

# Модульный тест!
def test_check():
    p1 = GenNum(10)
    assert p1.miller_rabin() == False