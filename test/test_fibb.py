import sys
sys.path.append('/CSC510-GROUP19/code/')
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