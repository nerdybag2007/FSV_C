def start_program():
    
        while True:
            def display_menu():
                print("1.add student")
                print("2.view student")
                print("3.search student")
                print("4.update student")
                print("5.delete student")
                print("6.exit ")
            display_menu()
            try:
                choice=int(input("enter your choice:"))
            except ValueError:
                print("invalid input please proceed with right value")
                continue
            if choice==6:
                print("thankyou for choosing studnet managemnet system")
                break
            elif 1<= choice<=5:
                print("feature coming soon")
            else:
                print("invalid choice pleasse try again")
start_program()
def add_student():
     




