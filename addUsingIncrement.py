def increment(num):
    '''
    Objective : to increment a number by 1
    Input parameters :
             numb  : Number to be incremented
    Return value : Incremented value of given number
    '''
    num=num+1
    return num


def add(num1,num2):
    '''
    Objective : To calculate the sum of two numbers
    Input parameters :
             num1 : first number input by user
             num2 : second number input by user
    Return value : Sum of given two numbers
    '''
    #Approach : Using increment function to compute sum of two numbers recursively

    assert num1>=0 and num2>=0 
    if num2==0:
        return num1
    else:
        return add(increment(num1),num2-1)
