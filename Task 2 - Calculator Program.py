# Calculator Program


def menu():
    while True:
        print("====SIMPLE CALCULATOR====")
        print("**The Operation Choices**")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        operation_choice = input("Enter your choice:")
        if operation_choice == "1":
            num1 = float(input("Enter the number 1:"))
            num2 = float(input("Enter the number 2:"))
            print(num1, "+", num2)
            print("Result:")
            print("The sum of number 1 and number 2:  ", num1 + num2)
        elif operation_choice == "2":
            num1 = float(input("Enter the number 1:"))
            num2 = float(input("Enter the number 2:"))
            print(num1, "-", num2)
            print("Result:")
            print("The difference of number 1 and number 2: ", num1 - num2)
        elif operation_choice == "3":
            num1 = float(input("Enter the number 1:"))
            num2 = float(input("Enter the number 2:"))
            print(num1, "*", num2)
            print("Result:")
            print("The multiplication of number 1 and number 2: ",num1 * num2)
        elif operation_choice == "4":
            num1 = float(input("Enter the number 1:"))
            num2 = float(input("Enter the number 2:"))
            print(num1, "/", num2)
            if num2 == 0.0:
                print("Division by Zero Error")
            else:
                print("Result:")
                print("The division of number 1  and number 2: ",num1 / num2)
        elif operation_choice == "5":
            print("exit..")
            exit()
        else:
            print("Invalid Choice!")


menu()




