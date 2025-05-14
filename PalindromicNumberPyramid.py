n=int(input("Enter Number : "))
for i in range(1, n + 1):
    print(" " * (n - i)*2, end="")
    start_num = i
    for j in range(start_num, start_num + i):
        print(j, end=" ")
    for j in range(start_num + i - 2, start_num - 1, -1):
        print(j, end=" ")
    print()





def pattern(i, n):
    if i > n:
        return
    spaces = ' ' * (n - i)*2
    increasing = [str(x) for x in range(i, 2*i)]
    decreasing = [str(x) for x in range(2*i - 2, i - 1, -1)]
    row = ' '.join(increasing + decreasing)
    print(spaces + row)
    pattern(i + 1, n)  
n = int(input("Enter Number: "))
pattern(1, n)  

n = int(input("Enter A Number : \n"))
for i in range(1, n+1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(i + j, end=" ")
    for j in range(i - 1):
        print(2 * i - j - 2, end=" ")
    print()  

