for row in range(0,7):
    for col in range(0,5):
        if(row==0)and(col in{1,2,3}):
            print("$",end=" ")
        elif(row in (1,2,4,5,6))and(col in{0,4}):
            print("$",end=" ")
        elif(row==3)and(col in{0,1,2,3,4}):
            print("$",end=" ")
        else:
            print(' ',end=' ')
    print()
