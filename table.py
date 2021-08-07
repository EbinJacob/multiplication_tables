while(1):
    print("- - - MULTIPLICATION TABLE GENERATOR - - -")
    print(" ")
    print("(To exit enter -1)")
    n = int(input("Enter a number to get the multiplication table: "))
    if n==-1:
        exit()
    val = int(input("Print multiplication tables upto: "))
    print(" ")
    for i in range(1,val+1):
        pro = i*n
        print(str(n)+" X "+str(i)+" = "+str(pro))
    print(" ")
    print(" ")
    