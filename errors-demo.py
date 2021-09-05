listt = ["1","2","5a","10b","abc","10","50"]

# Find the numbers inside of the list

# for x in listt:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue    


# Long as user doesn't enter 'q' value make sure every input is a number. If it is not a number write a error message

# while True:
#     number = input("Number: ")
#     if number == 'q':
#         break

#     try:
#         result = float(number)
#         print("Valid number : ",result)
#     except ValueError:
#         print("Invalid number")
#         continue        
# Give a Turkish character error in the password


# def checkPassowrd(password):

#     turkish_characters = "şçğüöıİ"



#     for i in password:
#         if i in turkish_characters:
#             raise TypeError("Password can't contain turkish characters")
#         else:
#             pass
#     print("Valid password")        


# password = input("Password: ")    

# try:
#     checkPassowrd(password)
# except TypeError as err:
#     print(err)    

# Make a factorial function. Give error messages for the coming value.

def factorial(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negative value")

    result = 1

    for i in range(1, x + 1):
        result *= i

    return result     


for x in [5, 10, 20, -3, '10a']:
    try:
        y = factorial(x)
    except ValueError as err:
        print(err)
        continue
print(y)                