#First of lets see how comments are created

print("hello world") # This is a comment here!

# Python oporators
Addition = "+"
Subtraction = "-"
Multiplication = "*"
Division = "/"
Remainder = "%"
Exponent = "**"

num1 = 2+2 
num2 = 4-5
num3 = 2*2
num4 = 3/6
num5 = 19%3
num6 = 2**4

print (num1)
print (num2)
print (num3)
print (float(num4))
print (num5)
print (int(num6))


a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
b = [" " * 2 * (7-i) + "very" * i for i in a]
for line in b:
    print(line)

# Veriables

x = 5
y = "aobot89"

print(x)
print(y)


# while loops ex 1

a = 0 
while a < 10:
    a = a + 1
    print (a)


# while loop ex 2
x = 10
while x != 0:
    print(x)
    x = x - 1
    print("wow, we´re counted x down, and now it equals", x)
    print("and now the loop had ended")

# boolean operators
    
# less than 
   # <
# less than or equal to
   # <=
# greater than
   # >
# greater than or equal to
   #>=
# not equal to
   # !=
# not equal to (alternate, != preferred)
   # <>
# equal to
   # ==

# if statement ex 1

y = 1
if y == 1:
    print("y still equal 1, i was just checking")

print("we will show the even number up to 20")
n = 1
while n <= 20:
    n = n + 1
    if n% 2 == 0:
        print(n)
print("there, done")


# else and elif statement

a = 1 
if a > 5:
    print("a is greater than 5")
else:
    print("a is less than 5")

z = 4
if z > 70:
    print("something is vary wrong")
elif z < 7:
    print("this is normal")


# indentation
    
a = 10 
while a > 0:
    print(a)  
    if a > 5:
        print("big number")
    elif a % 2 != 0:
        print("this is an odd number")
        print("it isn´t greater than 5")
    else:
        print("this number isn´t greater than 5")
        print("nor is it odd")
        print("feeling special?")
    a = a - 1
    print("we just made 'a' one less than what is was")
    print("and unless a is not greater than 0, we´ll do the loop again")
    print("well, it seems as if 'a' is now no bigger than 0")
    print("the loop is now over, and without further ado, so is this program")

    # test