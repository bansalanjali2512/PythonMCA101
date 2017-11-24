def areaCircle(radius):
    """
    Objective: Computes the area of a circle of the given radius
    Input Parameters:
        radius: Radius of the circle
    Return Value: Area of circle
    """
    area = 3.14*radius**2
    return area
    

def main():
    '''
    Objective: To find area of circle
    Input Parameters: None
    Return Value: None
    '''
    #approach: Using function areaCircle
    
    radius = int(input('Enter radius: '))
    area = areaCircle(radius)
    
    print("Area of a circle with radius ",radius," is: ", area)

if __name__=="__main__":
    main()
