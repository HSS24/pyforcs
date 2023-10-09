#assignment: conditionals
#made by hss

import platform
import os

def say_yes():
    for i in range(10):
        print("Yes it is!")

answer = input("Is today a good day? (y/n)")
if answer == "y":
    say_yes()