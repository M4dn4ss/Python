# x = 10

# if x > 5:
#     raise Exception("x can't be bigger than 5")

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Password must be at least 7 characters.")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Password must contain non-capital letters.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Password must contain capital letters.")  
#     elif not re.search("[0-9]",psw):
#         raise Exception("Password must contain number.") 
#     elif not re.search("[_@$]",psw):
#         raise Exception("Password must contain alpha numeric character.")
#     elif re.search("\s",psw):
#         raise Exception("Password can't contain space.")
#     else:
#         print("Valid password")     

# password = "123465678aA@" 

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)    
# else:
#     print("Valid password")    
# finally:
#     print("Validation has been completed")    


class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name has too many characters.")
        else:
            self.name = name


p = Person("Aliiiiiiiiiiiiii", 1989)                