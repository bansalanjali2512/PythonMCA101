import matplotlib.pyplot as plt

def recursivePlotSquare(x,y,size=0):
  '''
  Objective: To plot multiple squares
  Input Parameters: x, y - lists of x coordinates and y
  coordinates respectively
  Return Value: None
  '''
  #approach: Using recursion

  x = [0, size, size, 0, 0]
  y = [0, 0, size, size, 0]

  if (size == 1):
    return
  else:
    plotSquare(x,y)
    return recursivePlotSquare(x,y,size-1)

def plotSquare(x, y):
  '''
  Objective: To plot a square
  Input Parameters: x, y - lists of x coordinates and y
  coordinates respectively
  Return Value: None
  '''
  plt.plot(x, y, 'ro--')

def main():
  '''
  Objective: To plot a square based on user input
  Input Parameter: None
  Return Value: None
  '''
  size = int(input('Enter size of the square: '))
  if (size <= 0):
    print("Invalid Size..!")
    return

  x = [0, size, size, 0, 0]
  y = [0, 0, size, size, 0]
  recursivePlotSquare(x, y, size)
  plt.title('Square')
  plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
  plt.grid()
  plt.show()
  
if __name__ == '__main__':
  main()
