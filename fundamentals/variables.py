x = 5
y = "haytam"
print(x*y)

x=float(x)
print(type(x) ,"val : " ,x)

### assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

### unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

### Global var :
x= "awesome"

def myfunc():
  print("python is ? ," + x)
myfunc()  

### global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


