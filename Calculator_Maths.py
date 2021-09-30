'''imports'''
import time
from sys import exit

#Maths librarys
import math
import matplotlib
import baseConverter
import cmath
import fractions
import numpy
import random

from numpy.lib.function_base import append

'''main code'''


class Mathematics:
    num = 0
    def __init__(self, base):
        self.base = base
    
    def addition(self):
        self.num.split()
        addNum = math.fsum(self.num)   # fsum([2, 4, 0.5, 23.5]) # Layout needed for fsum()
    
    def subtraction(self):
        pass
    
    def multiplication(self):
        pass
    
    def percentage(self):
        pass
   
    def powers(self):
        pass
    
    def squareRoot(self):
        SQRTNum = math.sqrt(self.num)     # sqrt(x) format 
   
    def PInumber(self):
        PINum = math.pi #### 15 decimal places

    def logarithms(self, base):
        LogNum = (math.log(self.num, base))
   
    def naturalLog(self):
        NatLogNum = (math.log10(self.num) / math.log10(math.e))

    def factorial(self):
        pass
    
    def randomNum(self):
        pass
   
    def exponent(self):
        ExpNum = math.exp(self.num)