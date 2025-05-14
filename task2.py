def zigzag_pattern(n):
    spaces = [2,1,0]  
    index, direction = 0, 1 
    for i in range(n):
        print(' ' * spaces[index],end="")
        index += direction
        if index == len(spaces) or index < 0:
            direction *= -1
            index += 2 * direction  
        print('*')
n = int(input("Enter A Number Of Rows: \n"))
zigzag_pattern(n) 

