while(1):
    print("(To exit enter -1)")
    n = int(input("Enter a number to get the multiplication table: "))
    if n==-1:
        exit()
    for i in range(1,11):
        pro = i*n
        print(str(n)+" X "+str(i)+" = "+str(pro))
    