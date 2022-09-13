class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print("My name is " + p1.name + " my age is " + str(p1.age))
