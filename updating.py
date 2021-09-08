# with open("newFile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("test")   

# with open("newFile.txt","r+",encoding="utf-8") as file:
#     print(file.read())    

# Update at the end of the file

# with open("newFile.txt","a",encoding="utf-8") as file:
#     file.write("\nEmel Turan")

# Update at the start of the file

# with open("newFile.txt","r+",encoding="utf-8") as file:
#         content = file.read()
#         content = "Efe Turan\n" + content
#         file.seek(0)
#         file.write(content)
#         print(content)




# Updating at middle of the file
with open("newFile.txt","r+",encoding="utf-8") as file:
    listt = file.readlines()
    listt.insert(1,"Yılmaz Aygün\n")
    file.seek(0)
    file.writelines(listt)

with open("newFile.txt","r",encoding="utf-8") as file:
        print(file.read())        