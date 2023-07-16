import calculatorart
print(calculatorart.logo)
def ADDITION(a,b):
    return a+b
def SUBTRACTION(a,b):
    return a-b
def MULTIPLICATION(a,b):
    return a*b
def DIVISION(a,b):
    return a/b
operations={
    "+":ADDITION,
    "-":SUBTRACTION,
    "*":MULTIPLICATION,
    "/":DIVISION,
}
def calculator():
    num1=float(input("Enter the first number : "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        operations_symbol=input("Enter your choice ( + , - , * , / ) : ")
        num2=float(input("Enter the second number : "))
        calculation_function=operations[operations_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        choice=input(f"Type 'y' to continue calculating with the value {answer} and 'n' to start from beginning. To stop the calculator type 's'  : ").lower()
        if choice=="y":
            num1=answer
        elif choice=="n":
            should_continue=False
            calculator()
        else:
            return
calculator()