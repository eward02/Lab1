Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Elise Ward and Samantha Patin
print("Hello, World")
Hello, World
print("Welcome to CPSC 204")
Welcome to CPSC 204
print("Hello\nWorld")
Hello
World
print("How\nare\nyou?")
How
are
you?
print("Today", + "is" +, "Wednesday")
SyntaxError: invalid syntax
print("Today", "is", "Wednesday")
Today is Wednesday
print("Today", + "is" + "Wednesday")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("Today", + "is" + "Wednesday")
TypeError: bad operand type for unary +: 'str'
>>> print("Today"+"is"+"Wednesday")
TodayisWednesday
>>> TodayisWednesday
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    TodayisWednesday
NameError: name 'TodayisWednesday' is not defined
>>> print("a\nb\nc")
a
b
c
>>> print("Hello" + "World")
HelloWorld
>>> print("Hello\n"+"\nWorld!")
Hello

World!
>>> print("123\n45\n6")
123
45
6
>>> 1+2*3
7
>>> (1+2)*3
9
>>> 7/3
2.3333333333333335
>>> 7//3
2
>>> 7%3
1
>>> 22/4
5.5
>>> 22//4
5
>>> 22%4
2
>>> 3**2
9
>>> 2**3
8
>>> # predict (4+3)//2=3, 6%2=0
>>> (4+3)//2
3
>>> 6%2
0
>>> 1+2*3**4
163
>>> print("2+2=", 2+2)
2+2= 4
>>> print("2 + 2 = ",2+2)
2 + 2 =  4
>>> print("2 + 2 =",2+2)
2 + 2 = 4
>>> print("50 pounds is ",50*0.452592, "Kilograms")
50 pounds is  22.6296 Kilograms
