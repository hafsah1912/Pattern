# n=int(input("Enter Number : "))
# for i in range(n):
#     if(i==0):
#         print(" "*(n-i-1)+"*")
#         continue
#     elif(i==n-1):
#         print("* "*n)
#         continue
#     else:
#         print(" "*(n-i-1)+"*"+(" ")*(2*i-1)+"*")



# n=int(input("Enter A Number : "))
# print("Reversed")
# for i in range(n):
#     if(i==0):
#         print("* "*n)
#     elif(i==n-1): 
#         print(" "*i+"*")
#     else:
#         print(" "*i+"*"+" "*(2*(n-i-1)-1)+"*")




n = int(input("Enter Number : "))
pattern = []

for i in range(n):
    if i == 0:
        row = " " * (n - i - 1) + "*"
        pattern.append(row)
    elif i == n - 1:
        row = "* " * n
        pattern.append(row)
    else:
        row = " " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*"
        pattern.append(row)

output = "\n".join(pattern)
with open("output.txt", "w") as file:
    file.write(output)





 
# n=int(input("Enter A Number : "))
# for i in range(1,n+1):
#     s=""
#     for j in range(1,2*n):
#         if(i==1 and j%2!=0) or(i==j) or i+j==n*2:
#             s+="*"
#             continue
#         else:
#             s+=" "
#     print(s)





n = 7

s = 2 * n-2

for k in range(n, -1, -1):

    for m in range(s, 0, -1):

        print(end=" ")

    s = s + 1

    for m in range(0, k + 1):

        print("*", end=" ")

    print("")