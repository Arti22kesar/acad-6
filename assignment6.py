#Ques1.

for i in range(10):
   a=int(input("enter the values:"))
   print(i)


#Ques2.

while(True):
    print("arti")

#Ques3.

l=[]
a=int(input("Enters the values:"))
b=int(input("Enters the values:"))
l.append(a)
l.append(b)
print(l)
for i in l:
    print(i**2)


#Ques4.

l=(([1,2],("string"),[ 1.2,2.4]))
for i in (l):
    a=[]
    b=[]
    c=[]
    print(*l,sep="\n")
    break


#Ques5.
even = []
odd = []
for i in range(1,101):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("number is even",even)
print("number is odd",odd)

#Ques6.

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end="")
    print()


#Ques7.

dictionary = {"arti" : "name", "age" :" 23"}
for i in dictionary:
     dictionary.get(i)
     print(i)


#Ques8.

l=[]
for i in range(0,5):
    num=int(input("enters the number:"))
    l.append(num)
print(l)
l2=[]
a=int(input("enter the values:"))
x=l.index(3)
x=l.remove(3)
print(l)