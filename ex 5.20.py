#Exercise 5.20
#(Display a two-dimensional list in Tabular format) Define a function that receives a two-dimensional list and displays its contents in tabular format

#Define function that gets number of rows and columns and the values of each cell for the matrix.  It will also display the matrix and the row and column indices
def display_table():
    #establish local variables 
    rows = int (input('Enter the number of rows wanted: '))
    columns = int (input('Enter the number of columns wanted: '))
    matrix = []
    
    #for loop that reads user input and fills value of the matrix cell
    for a in range (rows):
        x = []
        for b in range (columns):
            x.append(int(input('Please enter a number: ')))
        matrix.append(x)
    #For loop that sets up the column indices for the matrix
    for z in range(1):
        print ('x|', end = ' ')
        for y in range (columns):
            print(y, end = ' ')
    print()
        
    #For loop that sets up the rows indices and prints the value in each cell      
    for i in range (rows):
        print(i, end = '| ')
        for j in range (columns):
            print(matrix[i][j], end = ' ')
        print()

#Call the function    
display_table()