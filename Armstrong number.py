i=int(input("enter any number"))
prashant=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if(prashant==sum):

    print("Armstrong")
else:
    print("not Armstrong")
