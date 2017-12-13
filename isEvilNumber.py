#Program to check a number is evil or not

def isEvilNumber(n,count=0):
	'''
	Objective: To find whether n is evil number or not
	    Evil number is the number with even no. of 1's in binary equivalent
	Input parameters:
		n: number to be checked for evil or not
		count: to count number of 1
	Return value: None
	'''
	if(number != 0):
		if(number%2 == 1):
			count += 1
		isEvilNumber(n//2, count)
	else:
		if(count%2 == 0):
			return True
		else:
			return False

def main():
    '''
    Objective: To find whether n is evil number or not
	    Evil number is the number with even no. of 1's in binary equivalent
    User Inputs: 
    	n: number to be checked for evil or not
    Return Value: None
    '''
    #approach: Using function isEvilNumber
    
    n = int(input('Enter a number: '))
    if(isEvilNumber(n)):
    	print(n, 'is an Evil number.!')
    else:
    	print(n, 'is not an Evil number.!')

if __name__=="__main__":
    main()
