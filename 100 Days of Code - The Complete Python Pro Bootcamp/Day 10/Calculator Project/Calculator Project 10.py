import art


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calculation_dictionary = {
    "+" : add ,
    "-" : subtract ,
    "*" : multiply ,
    "/" : divide
}
def calculator():
    print(art.logo)
    should_accumulate = True
    number1 = float(input("Enter your first number?: "))

    while should_accumulate:
        for symbol in calculation_dictionary:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("Enter your second number: "))
        answer = calculation_dictionary[operation_symbol](number1, number2)
        print(f" {number1} {operation_symbol} {number2} = {answer}")

        choice = input(f" Type 'y' to continue calculating with {answer} , or type 'n' to  start a new calculation: ")
        if choice == "y":
            number1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()