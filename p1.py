#Write a program to understand control structure of python
a=int(input("\nEnter first value:"))
b=int(input("\nEnter second value:"))

#if..else statement
if(a>b):
    print("\na is greater than b")
else:
    print("\nb is greater than a")
'''.....output.....

Enter first value:5

Enter second value:8

b is greater than a
......................'''

#if..elif..else statement
if(b>a):
    print("\nb is greater than a")
elif(a>b):
    print("\na is greater than b")
else:
    print("\na&b are equal")
'''...output......
b is greater than a
.................'''


#while statement
while(a>0):
    print("value of a is ",a)
    a=a-2
print("loop is completed")
'''....output.......
value of a is  5
value of a is  3
value of a is  1
loop is completed
........................'''


#for loop
sum=0
for i in range(1,b+1):
    sum=sum+i
print("sum of first ",b," numbers:",sum)
'''......output..........
sum of first  8  numbers: 36
........................'''


#break statement
for i in [1,2,3,4,5]:
    if(i==4):
        print("element found..")
        break
    print(i)
'''.............output.........
1
2
3
element found..
.......................'''


#Continue statement
n=0
while(n<=b):
    n=n+1
    if(n%2==0):
        continue
    print(n)
print("end of while loop.")
'''..............output.............
1
3
5
7
9
end of while loop.
..................................'''


#pass stateemt
for i in [1,2,3,4,5]:
    if(i==4):
        pass
        print("pass value when is ",i)
    print(i)
'''...........output............
1
2
3
pass value when is  4
4
5
..................................'''


    


    
          
