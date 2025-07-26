"""Basics"""
inches = float(input("Enter length in inches: "))
cm = inches * 2.54
print("Length in centimeters: {:.2f} cm".format(cm))

""""""
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit: {:.2f}°F".format(fahrenheit))

""""""
import math

radius = float(input("Enter radius of the sphere: "))
volume = (4/3) * math.pi * (radius ** 3)
print("Volume of the sphere: {:.2f}".format(volume))

""""""
hours_worked = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter hourly rate: "))

gross_pay = hours_worked * rate_per_hour
tax = gross_pay * 0.20
net_pay = gross_pay - tax

print("Gross Pay: ${:.2f}".format(gross_pay))
print("Net Pay: ${:.2f}".format(net_pay))

""""""

for i in range(1, 11):
    print(i)

""""""
while True:
    num = float(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    print("You entered:", num)

""""""
num = int(input("Enter an integer: "))

if 0 <= num <= 10:
    print("Range 1: 0 to 10")
elif 11 <= num <= 20:
    print("Range 2: 11 to 20")
elif 21 <= num <= 30:
    print("Range 3: 21 to 30")
elif 31 <= num <= 40:
    print("Range 4: 31 to 40")
else:
    print("Number is outside the specified ranges.")



"""Strings"""

def reverse_string(s):
    return s[::-1]

input_str = "1234abcd"
print("Reversed string:", reverse_string(input_str))

def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("No. of Upper case characters:", upper)
    print("No. of Lower case characters:", lower)

sample = 'The quick Brow Fox'
count_case(sample)

def is_palindrome(s):
    s_clean = s.replace(" ", "").lower()  # remove spaces, make lowercase
    return s_clean == s_clean[::-1]

test_str = "madam"
if is_palindrome(test_str):
    print(f"'{test_str}' is a palindrome.")
else:
    print(f"'{test_str}' is not a palindrome.")

"""Lists"""
def unique_list(lst):
    return list(set(lst))

example_list = [1, 2, 3, 3, 3, 3, 4, 5]
print("Unique List:", unique_list(example_list))

def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers:", get_even_numbers(sample_list))

def kth_largest(lst, k):
    lst_sorted = sorted(lst, reverse=True)
    return lst_sorted[k - 1]

sample_list = [10, 5, 8, 20, 2]
k = 2
print(f"{k}th largest element:", kth_largest(sample_list, k))

def is_list_palindrome(lst):
    return lst == lst[::-1]

sample_list = [1, 2, 3, 2, 1]
print("Is palindrome:", is_list_palindrome(sample_list))

shopping_list = [
    "milk", "bread", "eggs", "butter", "cheese",
    "apples", "bananas", "cereal", "juice", "yogurt"
]

print("Full shopping list:", shopping_list)
print("Item 2:", shopping_list[1])  # Index starts at 0
print("Item 8:", shopping_list[7])

item_to_add = input("Enter an item to add to the shopping list: ")
shopping_list.append(item_to_add)

print("Updated shopping list:", shopping_list)

"""Dictionary"""
sample_dict = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 7}


ascending = dict(sorted(sample_dict.items(), key=lambda x: x[1]))
print("Ascending by value:", ascending)

descending = dict(sorted(sample_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending by value:", descending)

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

key = input("Enter key to check: ")
if key in my_dict:
    print(f"'{key}' exists in the dictionary with value:", my_dict[key])
else:
    print(f"'{key}' does not exist in the dictionary.")

person = {'name': 'John', 'age': 25, 'job': 'Engineer'}

for key, value in person.items():
    print(f"{key}: {value}")

n = int(input("Enter the range of numbers: "))
squares = {x: x ** 2 for x in range(1, n + 1)}
print("Number-Square Dictionary:", squares)

employees = {}


for i in range(3):  # 3 is changable
    emp_no = input("Enter employee number: ")
    name = input("Enter employee name: ")
    position = input("Enter position: ")
    employees[emp_no] = {'name': name, 'position': position}

print("Employee Directory:")
for emp_no, data in employees.items():
    print(f"Employee #{emp_no} → Name: {data['name']}, Position: {data['position']}")

"""Functions"""
def square_number(n):
    return n ** 2

num = float(input("Enter a number: "))
result = square_number(num)

print("The square of the number is:", result)

def largest_number(a, b):
    if a > b:
        return a
    else:
        return b

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

largest = largest_number(x, y)
print("The largest number is:", largest)

"""OOP"""
"""Circle Class"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

"""Person Class"""
from datetime import datetime

class Person:
    def __init__(self, name, country, dob):  # dob format: 'YYYY-MM-DD'
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

p = Person("Alice", "Canada", "2000-04-15")
print("Name:", p.name)
print("Age:", p.get_age())

"""Calclator Class  """
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

calc = Calculator()
print("Add:", calc.add(10, 5))
print("Subtract:", calc.subtract(10, 5))
print("Multiply:", calc.multiply(10, 5))
print("Divide:", calc.divide(10, 5))

"""Shape class"""
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):  # sides of triangle
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

circle = Circle(3)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Circle area:", circle.area())
print("Square perimeter:", square.perimeter())
print("Triangle area:", triangle.area())
