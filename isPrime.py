#!/bin/python3

import sys

#function to check a number is prime or not
def isPrime(num):
    for i in range (2,num//2):
        if(num%i == 0):
            return False
    return True
    
def main():
    num = int(input('Enter a number: '))
    if(isPrime(num)):
        print('Number is prime.!')
    else:
        print('Number is not prime.!')

if __name__ == "__main__":
    main()
