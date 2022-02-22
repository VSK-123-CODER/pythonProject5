def calculator():
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    list = {"+": add, "-": subtract, "*": multiply, "/": divide}

    num1 = float(input("whats the first number ? "))
    num2 = float(input("whats the next number? "))
    for i in list:
        print(i)
    operation_symbol = input("pick an operation from line above")
    operation = list[operation_symbol]
    answer = operation(num1, num2)
    print(answer)

    calculating_over = False
    while not calculating_over:
        option = input("is calculating over? type 'Y' for yes and 'N' for no")
        if option == "N":
            num = float(input("whats the third number? "))
            operation_symbol = input("pick an operation ")
            operation = list[operation_symbol]
            answer = operation(answer, num)
            print(answer)
        else:
            calculating_over = True
            calculator()


calculator()

