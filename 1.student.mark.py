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