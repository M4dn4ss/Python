def calculate_mark(row):
    row = row[:-1]
    listt = row.split(":")

    studentName = listt[0]
    marks = listt[1].split(",")

    mark1 = int(marks[0])
    mark2 = int(marks[1])
    mark3 = int(marks[2])

    average = (mark1 + mark2 + mark3) / 3

    if average >= 90 and average <= 100:
        letter = "AA"
    elif average >= 85 and average <= 89:
        letter = "BA"  
    elif average >= 80 and average <= 84:
        letter = "BB"       
    elif average >= 75 and average <= 79:
        letter = "CB"         
    elif average >= 70 and average <= 74:
        letter = "CC"    
    elif average >= 65 and average <= 69:
        letter = "DC"     
    elif average >= 60 and average <= 64:
        letter = "DD"    
    elif average >= 50 and average <= 59:
        letter = "FD"        
    elif average >= 0 and average <= 49:
        letter = "FF"    
    return studentName + ": " + letter + "\n"              

def read_average():
    with open("Exam_Marks.txt","r",encoding="utf-8") as file:
        for row in file:
            print(calculate_mark(row))

def enter_mark():
    name = input("Student's name: ")
    lastName = input("Student's lastname: ")
    mark1 = input("Mark 1: ")
    mark2 = input("Mark 2: ")
    mark3 = input("Mark 3: ")

    with open("Exam_Marks.txt","a",encoding="utf-8") as file:
        file.write(name + " " + lastName + ":" + mark1 + "," + mark2 + "," + mark3 + "\n")

def save_marks():
    with open("Exam_Marks.txt","r",encoding="utf-8") as file:
        listt = []

        for i in file:
            listt.append(calculate_mark(i))

        with open("results.txt","w",encoding="utf-8") as file2:
            for i in listt:
                file2.write(i)    

while True:
    operation = input("1-Read Marks\n2-Enter Marks\n3-Save the marks\n4-Exit\n")

    if operation == '1':
        read_average()
    elif operation == '2':
        enter_mark()
    elif operation == '3':
        save_marks()
    else:
        break
