operator = input("Choose an operator: +,-,/,* ")
number1 = float(input("Choose a number "))
number2 = float(input("Choose a number "))

print(f"The choosen operator{operator}")
print(f"1st choosen number {number1}")
print(f"2nd choosen number {number2}")

def addition(number1, number2):
    return number1 + number2
def subtraction(number1, number2):
    return number1 - number2
def division(number1, number2):
    return number1 / number2
def multiplication(number1, number2):
    return number1 * number2
    

if operator == "+":
    print(f"The addition is equal to: {addition(number1, number2)}")
elif operator == "-":
    print(f"The substraction is equal to: {subtraction(number1, number2)}")
elif operator == "*":
    print(f"The multiplication is equal to: {multiplication(number1, number2)}")

elif operator == "/":
    print(f"The division is equal to: {division(number1, number2)}")

else:
    print(f"{operator} is not valid")





