x = 7  # integer no fawasil
y = 5.4  #double
z = "Hello"  #string
a = True  #boolean True or False

y = [x, y, z, a]  #array

# boolean

# logical operators
# ==, >, <, >=, <=, !=, or, and
# print("Answer: ",  3 > 4 and 5 >= 5)

# print( )

f = 5
sf7 = 4

# if statment
# if f == sf7:
#   print("f is equal to sf7")
#   print("inside If block")
# elif f == 4:
#   print("f is equal to 4")
#   print("inside elif block")
# else:
#   print("else block")

# print("outside if block")

# loops

## while
# i = 5
# while i > 0:
#   print(i)
#   i = i - 2

## do while

## for
# for i in y:
#   print(i)

# functions

# def power2(a):
#   print(a)
#   return a + a

# # print(power2(4) + 4)

# def printHello():
#   print("Hello")

# printHello()


# def findStringInIndex(arr, pos, value):
#   return arr[pos] == value

array = [1, 6, 4, 2, 5, 3]



# print(findStringInIndex())
# Class
class Person:
  def __constr__(self, name, age, height):
    self.name = name
    self.age = age
    self.height= height

  def sayHello(self):
    print("Hello my name is " + self.name)

  def sayAge(self):
    print("Hello my age is" , self.age)

  def setName(self, name):
    self.name = name

  def setAge(self, age):
    self.age = age

  def getAge(self):
    return self.age


p1 = Person()
p1.name = 'ibrahim'
p1.age = 23
p1.height = 175
p2 = Person()
p2.name = "Ali"
p2.age = 24
p2.height = 173
print(p1.name)
p1.setName("mohammad")
print(p1.name)
p1.setAge(25)
age = p1.getAge()
print(age)


'''
This is a block
comment
'''

y, d =3, "2"


y , d = d , y

print(y)
print(d)


# PEMDAS => Parentheses, Exponents, Multiplication, Division, Addition, Subtraction

number_1 = 1 - 3 ** 3 * (3 + 2 ** 2)
