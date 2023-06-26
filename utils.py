"""
작성일자 : 2022.09.08
코드네임 : utils.py
"""


def factorial(x):
    if x<= 1:
        return 1
    return x * factorial(x-1)


def gugudan(x):
    for i in range(9):
        print((i+1) * x)

