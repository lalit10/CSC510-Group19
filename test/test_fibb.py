import sys
sys.path.insert(1,'/CSC510-GROUP19/code/')
import fibonacci 

testInput = [1,2,3,4,5,6]
testOutput = [1,1,2,3,5]

success = 0
def testFibb(): #Function returns percentage of cases that are passing 
    for i in range(len(testOutput)):
        if testOutput[i] ==  fibonacci .fib(n):
            success += 1

    return success*100/len(testOutput)

testFibb()