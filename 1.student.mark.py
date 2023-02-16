#number of student
while True:
    try:
        nbstudent=int(input("How many student do they Have : "))
        break
    except:
        print("number of student unvailable")

#student infromation 
listnamestudent=[]
listdobstudent=[]
listidstudent=[]
for i in range (nbstudent):
    print("student n°",i+1," : ")
    idstudent=input("what is the student's id : ")
    listidstudent.append(idstudent)
    namestudent=input("what is the name of the student : ")
    listnamestudent.append(namestudent)
    dobstudent=input("what is the DoB of the student : ")
    listdobstudent.append(dobstudent)

#number of courses
while True:
    try:
        nbcourses=int(input("How many courses do they Have : "))
        break
    except:
        print("number of student unvailable")

#courses infromation
listidcourse=[]
listnamecourse=[]
for i in range (nbcourses):
    print("courses n°",i+1," : ")
    idcourse=input("what is the coruse's id : ")
    listidcourse.append(idcourse)
    namecourse=input("what is the name of the course : ")
    listnamecourse.append(namecourse)


#marks student
listmarks=[]
for i in listnamecourse:
    print("in",i,"...")
    for x in listnamestudent:
        print("what is the marks for",x," : ")
        marks=input("")
        listmarks.append(marks)
        