for row in range(7):
    for col in range(5):
        if(row in (0,6))and(col in{0,3}):
            print("s",end=" ")
        elif(row in (1,2,3,4,5,6))and(col in{0}):
            print("s",end=" ")
        elif(row in (1,5))and(col in{0,2}):
            print("s",end=" ")
        elif(row in(2,4))and(col in{0,1}):
            print("s",end=" ")
        else:
            print(' ',end=' ')
    print()
