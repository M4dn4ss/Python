# class

class Person:    
    # class attributes
    address = 'no information'
    # constructor 
    def __init__(self, name, year):
        
        # object atributes
        self.name = name
        self.year = year
        print('init method worked')

        # methods


# object (instance)
p1 = Person(name ='ali',year = 1990)
p2 = Person(name ='Sam',year = 2000)
# updating
p1.name = 'Samuel'
p1.address = 'New York'
# accession object attributes
print(f'p1 name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 name: {p2.name} year: {p2.year} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)