#!/bin/python3

import sys

#function to check a number is prime or not
def isPrime(num):
    for i in range (2,num//2):
        if(num%i == 0):
            return False
    return True
    
#function to find difference of highest and lowest prime no's
def maxDifference(startVal, endVal):
    # Complete this function
    minPrime = 0
    maxPrime = 0
    for i in range(startVal,endVal):
        if(isPrime(i)):
            minPrime = i
            break
        
    for i in range(endVal,startVal,-1):
        if(isPrime(i)):
            maxPrime = i
            break
    return maxPrime - minPrime

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        startVal, endVal = input().strip().split(' ')
        startVal, endVal = [int(startVal), int(endVal)]
        result = maxDifference(startVal, endVal)
        print(result)
