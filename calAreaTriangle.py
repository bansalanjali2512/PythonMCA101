#P3. WAP to print area of triangle taking base & height of triangle as user inputs.
def areaTriangle(base, height):
    '''
    Objective : To compute the area of a triangle
    Input Parameters :
        base: Base of triangle
        height: Height of triangle
    return: area of triangle
    '''
    #approach: multiply 0.5 and base and height
    
    area = 0.5*base*height
    return area

def main():
    '''
    Objective : to compute the area of a triangle
    User Inputs :
        base: Base of triangle
        height: Height of triangle
    '''
    #approach: use function areaTriangle
    
    base = int(input('Enter base of Triangle: '))
    height = int(input('Enter Height of Triangle: '))
    print('base of Triangle: ', base)
    print('Height of Triangle: ', height)
    print('Area of Triangle: ', areaTriangle(base, height))
    print('End of Output')

if __name__ == '__main__':
    main()
    print('Program Ends..!')
