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
end=False
while end!=True:
    num1=int(input("Enter the first number : "))
    for symbol in operations:
        print(symbol)
    operations_symbol=input("Enter your choice ( + , - , * , / ) : ")
    num2=int(input("Enter the second number : "))
    calculation_function=operations[operations_symbol]
    answer=calculation_function(num1,num2)
    print(f"{num1} {operations_symbol} {num2} = {answer}")
    stop=input("Do you want to start again (yes/no) : ")
    if stop=="no":
        end=True