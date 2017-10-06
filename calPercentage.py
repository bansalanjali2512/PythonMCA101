#P5. WAP to compute & print percentage taking max marks and obtained marks as user inputs.
def calPercentage(obtained_marks,max_marks):
    '''
    Objective : To calculate percentage of a student
    Input Parameters :
        obtained_marks : total marks obtained by student in exams
        max_marks : maximum marks a student can obtain
    Return Value : Return the computed percentage
    '''
    #approach : divide obtained_marks by max_marks and multiply the result by 100
    
    percentage = (obtained_marks/max_marks)*100
    return percentage
    
def main():
    '''
    Objective : To calculate percentage of a student
    User Inputs :
        obtained_marks : total marks obtained by student in exams
        max_marks : maximum marks a student can obtain
    Return Value : None
    '''
    #approach : computing percentage using cal_percentage function
    
    obtained_marks = float(input('Enter the marks obtained by student : '))
    max_marks = float(input('Enter the maximum marks of the exam : '))
    print('Obtained Marks : ',obtained_marks)
    print('Maximum marks  : ',max_marks)
    print('The percentage obtained by the student is : ',caLPercentage(obtained_marks,max_marks),'%')
    
if __name__=='__main__':
    main()
    print('Program Ends..!')
