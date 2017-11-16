from unitconvert import temperature
from unitconvert import distance
import pytest

def miles_to_kilometers_test():
    assert miles_to_kilometers(1)==1.609
    
     
def kilometers_to_miles_test():
    assert kilometers_to_miles(1)==0.621371
    
    
def celsius_to_fahrenheit_test():
    assert celsius_to_fahrenheit(1)==((9/5))+32
    
    
def fahrenheit_to_celsius_test():
    assert fahrenheit_to_celsius(1) ==(5/9)-32   
    
