while True:
    def main():
        def input_num():
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            return a, b

        def sum():
            a,b=input_num()
            add=a+b
            print("Sum =", add)
            
        def mul():
            a,b=input_num()
            multiply=a*b
            print("Multiply =", a * b)
    

        op = input("Enter operation (+ or *): ")
        match op:
                    case '+':
                        sum()
                    case '*':
                     mul()
                    case _:
                        print("Invalid input")

    main()

