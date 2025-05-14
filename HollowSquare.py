# n=int(input("Enter number : "))
# for i in range(n):
#     s=""
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             s+="* "
#         else:
#             s+="  "
#     print(s)

n = int(input("Enter number: "))

for i in range(n):
    if i == 0 or i == n - 1:  
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "*") 

