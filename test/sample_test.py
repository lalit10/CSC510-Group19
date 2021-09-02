import sys
import os
sys.path.insert(1,'../../CSC510-GROUP19/code/')
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
new_path = os.path.join(parentdir, "code", "")
sys.path.insert(1,parentdir)
sys.path.insert(2,new_path)
import fibonacci

def func(x):
    return x + 1


def test_answer():
    assert fibonacci.fib(3) == 2