# error handling 

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print("You entered wrong input")
#     print(e)  


# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except:
#     print("You entered wrong input")

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("You entered wrong input",ex)

    else:
        print("Everything is good")
        break    
    finally:
        print("try except stopped")    

