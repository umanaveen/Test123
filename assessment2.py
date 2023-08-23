print("Question:1")
# varible define
value = 407
temp=value
sum = 0
# loop  Define
while temp > 0:
   cal = temp % 10
   sum += cal*cal*cal  
   temp = temp//10
  
# Condition Check
if sum == value:
  print("It Ia a Armstrong Number")
else:
 print("It Is Not a Armstrong Number")




# varible define
value2 = 8794
temp2=value2
num_len=len(str(value2))
sum2 = 0
# loop  Define
while temp2 > 0:
   cal2 = temp2 % 10
   sum2 += cal**num_len
   temp2 = temp2//10
# Condition Check

if sum2 == value2:
  print("It Is a Armstrong Number")
else:
 print("It Is Not a Armstrong Number")



print("Question:2")
# varible define
prime_val=2
if  prime_val>1:
       for i in range(2,prime_val):
        #Check if prime number
           if(prime_val % i) == 0:
              #print Result
              print(prime_val, "Is Not a Prime Number")
              break
       else:
        print(prime_val, "Is a Prime Number")


# varible define
prime_val2=6
if  prime_val2>1:
       for i in range(2,prime_val2):
        #Check if prime number
           if(prime_val2 % i) == 0:
              #print Result
              print(prime_val2, "Is Not a Prime Number")
              break
       else:
        print(prime_val2, "Is a Prime Number")


print("Question:3")
# define variable 2 varable of interval  
prime_start=2
prime_end=500

# prime_start=int(input("Enter Start no "))
# prime_end=int(input("Enter End no "))

print("The Prime no Between 1 To 1000 is:")
# Empty Array of list variable define
primelist=[]
for n in range(prime_start, prime_end + 1):
    if prime_start > 1:
      #  condition check
       for i in range(2,n):
           if (n % i) == 0:
            break
       else:
      #   prime no append
        primelist.append(n)
print(primelist)




print("Question:4")
# define variable for loop 
fib_num = 10;  
result=[]
# define function
def fibonacci_number(fib_num):

   #condition check
   if fib_num==0:
      return 0
   elif fib_num ==1:
      return 1
   else:
      return(fibonacci_number(fib_num-1)+fibonacci_number(fib_num-2))
print(f"The {fib_num} th Fibonacci Number is ")
for i in range(1,fib_num):
    #function calling
    resultVal= fibonacci_number(i)
    result.append(resultVal)
print(result)




print("Question:5")
# Define 2 input variable 
from_val=1
to_val=1000
perfect_arr=[]
print(f"Perfect number {from_val} To {to_val}")
# check perfect number
for num in range(from_val ,to_val):
   sum=0
   for n in range(1,num):
      if(num % n==0):
         sum=sum+n
   if(sum==num):
      #Displey Result
      perfect_arr.append(num)
print(perfect_arr)










