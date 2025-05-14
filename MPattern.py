
n = int(input("Enter number: "))
for i in range(1,4):
    s=""
    for j in range(1,n+1):
        a=i+j
        if(a>=0 and(a//4)*4==a):
            s+="*"
            continue
        if(i==2 and (j-4)>=0 and ((j-4)//4)*4==(j-4)):
            s+="*"
            continue
        s+=" "
    print(s)





n = int(input("Enter number: "))
for i in range(1,4):
    s = ""
    for j in range(1, n + 1):
        a = i + j
        if (a // 4) * 4 == a or (i == 2 and (j - 4) // 4 * 4 == (j - 4)):
            s += "*"
        else:
            s += " "
    print(s)
