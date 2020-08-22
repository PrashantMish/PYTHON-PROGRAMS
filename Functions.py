# function Creation
'''
def name(x,y):

    Name = input("Enter Your Name ") # input always takes input as string (Datatype).
    print(type(Name))
    print("Name")
    print(Name)


    c = x+y
    print("Addition is ->",c)
#function Call
a = int(input("Enter any Number"))
b = int(input("Enter any Number"))
name(a,b)
'''
# String Based Question

#string =  input("Enter any String ")#"going"  input
# output -> "gniog"]
sentance = "My Friend is going to the Collage".split()
print(sentance)
for string in sentance:
    l = len(string)
   # print(string,end = "")
    if l > 3:
        print(string[0] + string[l - 2:0:-1] + string[-1],end = " ")
    else:
        print(string,end= " ")
    # print(string[start:end:steps])
    #print(type(string))