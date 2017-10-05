def insertInSortedList(list1,element,index=0):
    '''
    Objective : To insert an element in a sorted list
    Input Parameters :
      list1 : User entered sorted list 
      element : Element to be inserted in list1
      index: Index
    Return Value : Sorted list after inserting element
    '''
    #approach : By using recursion
    
    if(element<list1[index]):
        list1.insert(index,element)
        return list1
    elif(index==len(list1)-1):
        list1.append(element)
        return list1
    else:
       return insertInSortedList(list1,element,index+1)
    
def main():
    '''
    Objective: To insert an element in a sorted list 
      in such way that list remains sorted
    Input Parameters: 
      list1: Sorted list
      element: Element to be inserted
    Return Value: None
    '''
    #approach: By using insertInSortedList() function
    
    list1=[int(x) for x in input("Enter list in ascending order: ").split()]
    element=int(input("Enter element to be inserted: "))
    print("List After Insertion Is : ")
    print(insertInSortedList(list1,element))
    
if __name__=='__main__':
    main()
