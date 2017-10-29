def mergeSortedLists(list1, list2, mergedList=[], index1=0, index2=0):
    '''
    Objective: To merge to sorted lists
    Input Parameters:
      list1: First sorted list
      list2: Second sorted list
      mergedList: Merged list
      index1: Index to traverse list1
      index2: Index to traverse list2
    Return: None
    '''
    #approach: Using recurssion
    
    
if (index1==(len(list1)) and index2==(len(list2))):
        return mergedList      
    elif ((index1!=len(list1) and index2==(len(list2))) or (list1[index1] <= list2[index2])):
        mergedList.append(list1[index1])
        return mergeSortedLists(list1,list2,mergedList,index1+1,index2)
    elif ((index1==(len(list1)) and index2!=len(list2)) or (list1[index1] > list2[index2])):
        mergedList.append(list2[index2])
        return mergeSortedLists(list1,list2,mergedList,index1,index2+1)


def main():
    list1=[int(x) for x in input("Enter sorted list1: ").split()]
    list2=[int(x) for x in input("Enter sorted list2: ").split()]
    print("Merged sorted list: ",mergeSortedLists(list1,list2))

if __name__=="__main__":
    main()
