#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created by hss24

f_n = int(input("what is the first number?"))
activity = input("what activity? (+ - * /)")
s_n = int(input("what is the second number? "))    

if activity == "+":
    print(f_n + s_n)

if activity == "-":
    print(f_n - s_n)

if activity == "*":
    print(f_n * s_n)

if activity == "/":
    print(f_n / s_n)
