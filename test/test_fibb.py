import sys
import os
## Code to run fib module from test
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
new_path = os.path.join(parentdir, "code", "")
print("New path:",new_path)
sys.path.insert(1,new_path)

import fibonacci 


def testFibb(): #Function returns percentage of cases that are passing
    testInput = [1,2,3,4,5]
    testOutput = [1,1,2,3,5]
    success = 0
    for i in range(len(testOutput)):
        if testOutput[i] ==  fibonacci .fib(testInput[i]):
            success += 1

    assert success == len(testOutput)

testFibb()