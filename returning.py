def exponentiation(number):   

    def inner(power):
        return number ** power

    return inner    

two = exponentiation(2) # 2-3
three = exponentiation(3)    # 3-4
print(two(3))
print(three(4))

def interrogate_authorization(page):
    def inner(role):
        if role == "Admin":
            return "{0} role can access to {1} page.".format(role,page)
        else:
            return "{0} role can't access to {1} page.".format(role,page)   
    return inner        

user1 = interrogate_authorization("Product Edit")        
print(user1("Admin"))
print(user1("User"))


def operation(operation_Name):
    def sum(*args):
        sum = 0
        for i in args:
            sum += i
        return sum

    def multiply(*args):
        product = 1
        for i in args:
            product *= i

        return product

    if operation_Name == "sum":
        return sum
    else:
        return multiply

adding = operation("sum")
print(adding(1,3,5,6,7))

multiplying = operation("multiply")
print(multiplying(1,2,3,4,6))
