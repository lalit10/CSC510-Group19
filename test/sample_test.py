#This file will contain test cases.
#import pytest
import sys
#sys.path.append('/CSC510-GROUP19/code/')
sys.path.insert(1,'/CSC510-GROUP19/code/')
import fibonacci

def func(x):
    return x + 1


def test_answer():
    assert fibonacci.fib(3) == 2