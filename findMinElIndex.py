#function  to find the index of the minimum element in list in the range of given indexes

def findMinElIndex(list,minElIndex=0,position=0):
    '''
    Objective: To find the index of minimum element
    Input Parameters:
           list: list in which index of minimum element is to be found
           minElIndex: Index of minimum element of list
           position: To traverse each element of list
    Return Value:  minimum element of the list
    '''
    #Approach: Traverse each element of list recursively
    
    lastIndex=len(list)-1
    if (position < lastIndex):
        if (list[minElIndex] > list[position+1]):
            minElIndex = position+1
        return findMinElIndex(list,minElIndex,position+1)        
    else:
        return minElIndex

#Test Case 1: Checking upper bound
list1=[34,56,29,16,7]
print(findMinElIndex(list1))

#Test Case 2: Checking lower bound
list1=[2,34,56,29,16,7]
print(findMinElIndex(list1))

#Test Case 3: Checking intermediate element
list1=[34,56,3,29,16,7]
print(findMinElIndex(list1))
