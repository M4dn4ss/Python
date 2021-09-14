import os
import datetime

result = dir(os)
result = os.name

# Change directory
os.chdir('C:\\')
os.chdir('../..')

# Create file
os.mkdir("newdirectory")

# Gives active directory
result = os.getcwd()
os.makedirs("newdirectory/newfile")
os.rename("newdirectory","newfiles")
os.rmdir("file")
os.removedirs("newfiles/newfile")

# listing
result = os.listdir()
result = os.listdir('C:')

for file in os.listdir():
    if file.endswith('.py'):
        print(file)

result = os.stat('date.py')
result = result.st_size/1024
result = datetime.datetime.fromtimestamp(result.st_ctime) # date of creating the file
result = datetime.datetime.fromtimestamp(result.st_atime) # date of last access
result = datetime.datetime.fromtimestamp(result.st_mtime) # date of changing

os.system("notepad.exe")

# path

result = os.path.abspath("_os.py")
result = os.path.dirname("D:/Projeler\Python/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("D:/Projeler\Python/_os1.py")
result = os.path.exists("D:/Projeler\Python")
result = os.path.isdir("D:/Projeler\Python")
result = os.path.isdir("D:/Projeler\Python")
result = os.path.isfile("D:/Projeler\Python/_os.py")
result = os.path.join("C:\\","test","test1")
result = os.path.split("C:\\test")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)