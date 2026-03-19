user_grade ={"Akash":"A", "Bindu" :"B"}

flag = True

while(flag):

    print("\nSelect option number from the below list to proceed Ahead : ")
    print("_____________________________________________________________\n")
    print("1 . Add a new Student and Grade ")
    print("2 . Update a existing Student Grade ")
    print("3 . Print all Students Grade ")
    print("4 : Exit")

    choice = int(input("\nEnter your option here :  "))

    if choice == 1 :
        name = input("Enter Student name : ")
        grade = input("Enter Student grade : ")
        user_grade[name]=grade
        print("The entry has been successfully added")

    elif choice == 2 :
        name = input("Enter Student name : ")
        grade = input("Enter updated Student grade : ")
        user_grade[name]=grade
        print("The entry has been successfully updated")


    elif choice == 3 :
        print("Student Name\tGrade")
        for key,value in user_grade.items():
            print( key +"\t\t"+ value)

    elif choice == 4 :
        print("Thanks for Using the Program\n")
        flag = False
    else :
        print(" Invalid Choice")