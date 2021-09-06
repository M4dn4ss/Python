# "w" : Writing

file = open("newFile.txt","w")
file = open("D:\Projeler/newFile2.txt","w")
file.close()

file = open("newFile.txt","w",encoding='utf-8')
file.write("Samedş")
file.close()


# "a" : Append

file = open("newFile.txt","a",encoding='utf-8')
file.write("Ali\n")
file.close()

# "x" : Create

file = open("newFile2.txt","x",encoding='utf-8')

