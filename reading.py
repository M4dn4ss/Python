try:
    file = open("newFile.txt","r")
    print(file)
except FileNotFoundError:
     print("Reading file error")    
finally:
     print("File closed")
     file.close()

file = open("newFile.txt","r",encoding="utf-8")

for i in file:
    print(i,end="")

# read() function
content1 = file.read()

print("Content 1")
print(content1)


file = open("newFile.txt","r",encoding="utf-8")
content2 = file.read()
print("Content 2")
print(content2)

content = file.read(5)
content = file.read(3)
content = file.read(3)
print(content)

# readline() function

print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline())
print(file.readline())


# readlines() function

listt = file.readlines()
print(listt[0])
print(listt[1])
print(listt[2])



file.close()
