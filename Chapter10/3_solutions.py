# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Attribute:
    a = 17


object = Attribute()
print("Object:", object.a)
print("Class:", Attribute.a)
object.a = 0
print("Object:", object.a)
print("Class:", Attribute.a)
