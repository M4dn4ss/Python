def adding(a,b):
    return a + b
def substracting(a,b):
    return a - b
def multiplying(a,b):
    return a * b
def dividing(a,b):
    return a / b

def operation(f1, f2 ,f3, f4, operation_Name):
    if operation_Name == "adding":
        print(f1(2,3))
    elif operation_Name == "substracting":
        print(f2(5,3))
    elif operation_Name == "multiplying":
        print(f3(3,4))
    elif operation_Name == "dividing":
        print(f4(10,2))
    else:
        print("Invalid operation")

operation(adding,substracting,multiplying,dividing,"adding")
operation(adding,substracting,multiplying,dividing,"substracting")
operation(adding,substracting,multiplying,dividing,"multiplying")
operation(adding,substracting,multiplying,dividing,"dividing")
operation(adding,substracting,multiplying,dividing,"a")