"""LAB 1 """
""" 1 """
radius = int(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print(f"The area of the circle with radius {radius} is: {area}")

""" 2 """
number = int(input("Enter a number to check it: "))
if number % 2 == 0:
    print(f"{number} is an even number.") 
else:
    print(f"{number} is an odd number.")      

""" 3 """
int1= int(input("Enter the first integer: "))
int2= int(input("Enter the second integer: "))      
int3= int(input("Enter the third integer: "))
if int1 == int2 or int1==int3 or int2==int3:
    print("The sum is 0")
else:
    sum = int1 + int2 + int3
    print(f"The sum of the three integers is: {sum}") 

""" 4 """
print("What is the max number you want ?")
n = int(input())
for i in range(1, n):
    for  j in range(1,i+1):
        print(j ,end=" ")
        if( j < i):
            print("+" ,end=" ")

""" 5  """
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

""" 6 """
for i in range (17):
    print(i ** 2)

""" 7 """
def even_generator(start=1 , end=100):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i  
            """ like return but its iterable dont exit from loop before ending its iterations """ 
even_generator(100 , 2000)