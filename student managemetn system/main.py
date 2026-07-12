def start_program():
    
        while True:
            def display_menu():
                print("add student")
                print("view student")
                print("search student")
                print("update student")
                print("delete student")
                print("exit student")
            try:
                choice=int(input("enter your choice:"))
            except ValueError:
                print("invalid input please proceed with right value")
            if choice==6:
                print("thankyou for choosing studnet managemnet system")
                break
            elif 1<= choice<=5:
                print("feature coming soon")
            else:
                print("invalid choice pleasse try again")
start_program()
        

