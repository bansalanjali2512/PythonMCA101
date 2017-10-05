#P2. WAP to print area of rectangle taking length & breadth of rectangle as user input.
def areaRectangle(length, breadth):
    '''
    Objective : To compute the area of a rectangle
    Input Parameters :
        length : length of rectangle
        breadth : breadth of rectangle
    Return Value : Area of rectangle
    '''
    #approach : multiply length and breadth
    area = length*breadth
    return area

def main():
    '''
    Objective : To compute the area of a rectangle
    User Inputs :
        length : length of rectangle
        breadth : breadth of rectangle
    Return Value : None
    '''
    #approach: use function areaRectangle
    
    length = int(input('Enter Length of Rectangle: '))
    breadth = int(input('Enter Breadth of Rectangle: '))
    print('Length of Rectangle: ', length)
    print('Breadth of Rectangle: ', breadth)
    print('Area of Rectangle: ', areaRectangle(length, breadth))
    print('End of Output')

if __name__ == '__main__':
    main()
    print('Program Ends..!')
