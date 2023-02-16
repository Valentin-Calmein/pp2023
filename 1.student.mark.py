#number of student
while True:
    try:
        nbstudent=int(input("How many student do they Have : "))
        break
    except:
        print("number of student unvailable")

#student infromation 
for i in range (nbstudent):
    print("student n°",i+1," : ")
    idstudent=input("what is the student's id : ")
    namestudent=input("what is the name of the student : ")
    dobstudent=input("what is the DoB of the student : ")

#number of courses
while True:
    try:
        nbcourses=int(input("How many courses do they Have : "))
        break
    except:
        print("number of student unvailable")

#courses infromation
for i in range (nbcourses):
    print("courses n°",i+1," : ")
    idcourse=input("what is the coruse's id : ")
    namecourse=input("what is the name of the course : ")