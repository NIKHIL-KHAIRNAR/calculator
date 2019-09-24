import Addition

class calculator:
    print("choose option : ")
    print("1. Addition")
    print("2. Subtract")
    print("3. Division")
    n = int(input("select option: "))
    if(n==1):
        print("Addition is selected")
        num1 = int(input("Enter the number:"))
        num2 = int(input("Enter the number:"))
        obj = Addition(num1, num2)
    if(n==2):
        print("Subtraction is selected")
    if(n==3):
        print("Division is selected")
