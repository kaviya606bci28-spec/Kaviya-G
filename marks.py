S=int(input("enter the mark1:"))
K=int(input("enter the mark2:"))
M=int(input("enter the mark3:"))
G=int(input("enter the mark4:"))
total=S+K+M+G
print("the total mark is:",total)
aggregate=total/400*100
print("the percentage is:",aggregate)
if(aggregate>75):
    print("distinction")
elif(60<=aggregate>75):
    print("first division")
elif(50<=aggregate>60):
    print("second division")
elif(40<=aggregate>50):
    print("third division")
else:
    print("fail")
