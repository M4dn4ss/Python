# # class

# class Person:    
#     # class attributes
#     address = 'no information'
#     # constructor 
#     def __init__(self, name, year):
        
#         # object atributes
#         self.name = name
#         self.year = year        

#     # instance methods
#     def intro(self):
#         print('Hello There. I am ' + self.name)

#     # instance methods
#     def calculateAge(self):
#         return 2019 - self.year    


# # object (instance)
# p1 = Person(name ='ali',year = 1990)
# p2 = Person(name ='Sam',year = 2000)

# p1.intro()
# p2.intro()

# print(f'my name is : {p1.name} and my age is : {p1.calculateAge()}')
# print(f'my name is : {p2.name} and my age is : {p2.calculateAge()}')

class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    # Methods
    def calculatePerimeter(self):
        return 2 * self.pi * self.radius    

    def calculateArea(self):
        return self.pi * (self.radius ** 2)

c1 = Circle() # radius = 1
c2 = Circle(5)

print(f'c1 : area = {c1.calculateArea()} perimeter = {c1.calculatePerimeter()}')
print(f'c2 : area = {c2.calculateArea()} perimeter = {c2.calculatePerimeter()}')