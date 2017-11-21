'''
    Function to find largest element in list till the user entered limit
    and place the largest element at limit index
'''

def findLargestElement(myList, limit, index = 0):
    '''
    Objective: To find largest element till limit and swap it to the
               index indicated by limit
    Input Parameters: 
        myList: List to be checked for largest element
        limit: Index upto which we need to traverse the myList
        index: To access elements of myList
    Return Value: Modified myList
    '''
    #approach: By swapping if preceeding element is larger and traverse recursively

    assert limit >= 0 and limit < len(myList)

    if index == limit:
        return myList
    elif myList[index] > myList[index+1]:
        temp = myList[index]
        myList[index] = myList[index+1]
        myList[index+1] = temp
        return findLargestElement(myList, limit, index+1)
    else:
        return findLargestElement(myList, limit, index+1)

def main():
    '''
    Objective: To find largest element till limit and swap it to the
               index indicated by limit
    Input Parameters: None
    Return Value: None
    '''
    #approach: Using function findLargestElement
    
    myList = [int(x) for x in input("Enter list: ").split()]
    limit = int(input('Enter limit: '))
    print("Modified list: ",findLargestElement(myList,limit))

if __name__=="__main__":
    main()
