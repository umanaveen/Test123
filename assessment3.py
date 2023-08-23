print("Question:1")
# Funcation define
def sumofsquare(num):
    sum_val=0
    # call loop
    for i in range(1,num+1):
        sum_val +=i*i
    return sum_val
# display output
# define variable
# a=4
a = int(input("Enter number for sum of Square value "))
print(f"The sum of squares 1 to", a ,"numbers  is:",sumofsquare(a))


print("Question:2")
# Funcation define
prod_cal=0
def prodctnum(x,y,z):
    prod_cal =x*y*z
    return prod_cal
# display output
# define variable
# x=2
# y=4
# z=6
x= int(input("Enter product of first no "))
y= int(input("Enter product of second no "))
z= int(input("Enter product of third no "))
print(f"The Product of Number:",[x,y,z], "Result :",prodctnum(x,y,z))


print("Question:3")
# Define function
def evennumbers(start,end):
    # between 2 no loop
    
    for i in range(start,end):
        res=[]
        # checking even no condition
        if i % 2==0:
            print(i, end=" ")
# start=2
# end =25    
start= int(input("Enter Even Start With "))
end= int(input("Enter Even End With  "))
print(f"the Even number between" ,start ,"To",end, "is" )
print(evennumbers(start,end))


print("Question:5")
# define function
def is_armstrongcheck(number):
    temp=number
    sumval= 0
    cal = temp % 10
    sumval += cal*cal*cal  
    temp = temp//10

# Input
n = int(input("Enter Armstrong number: "))
# Condition Check
if is_armstrongcheck(n):
  print(f"{n},Is a Armstrong Number")
else:
 print(f"{n}, Is Not a Armstrong Number")