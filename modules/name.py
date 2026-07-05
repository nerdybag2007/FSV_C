def main():
    calculation(1,"+",2)
def calculation(n1,op,n2):
    match op:
        case"+":sum(n1,n2)
        case"-":sub(n1,n2)
        case"/":div(n1,n2)
        case"*":mul(n1,n2)
def sum(n1,n2):
    print("sum =",n1+n2)
def mul(n1,n2):
    print("multiplying=",n1*n2)
def sub(n1,n2):
    print("Diff =",n1-n2)
def div(n1,n2):
    print("Div =",n1/n2)
if __name__ == "__main__":
    main()