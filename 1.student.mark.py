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
    idcourse=input("what is the course's id : ")
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
        
#print fonction
choice=0
while choice!=2:
    print("\n what do you want to do?")
    while True:
        choice=int(input("1-Show student marks for a given course \n2-Exit : "))
        if choice==1 or choice==2:
            break
        else:
            print("please, choose between 1 or 2")
#show marks for one course
    if choice==1:
        print("witch course do you want ?\n",listnamecourse)
        course=int(input("choose a number (1 for 1st, 2 for 2nd...): "))
        for i in range (len(listnamecourse)):
            if course==i:
                print("\nin",listnamecourse[i],"...")
                start=(course-1)*len(listnamecourse)
                end=len(listnamestudent)
                listmark=[]
                for i in range(start,end):
                    listmark.append(listmarks[i])
                for i in range (len(listmark)):
                    print(listnamestudent[i],"have",listmark[i])
        print("\nbye")
                
 #exit                    
    elif choice==2:
        print("\nThank you bye\n")
        break
        