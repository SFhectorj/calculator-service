
def add(str):
    split = str.split(',')
    num1 = split[0]
    num2 = split[1]

    return int(num1) + int(num2)

def sub(str):
    split = str.split(',')
    num1 = split[0]
    num2 = split[1]

    return int(num1) - int(num2)

def mult(str):
    split = str.split(',')
    num1 = split[0]
    num2 = split[1]

    return int(num1) * int(num2)

def div(str):
    split = str.split(',')
    num1 = split[0]
    num2 = split[1]
    if int(num2) == 0:
        return 'ERROR'
    else:
        return int(num1) / int(num2)


while True:
    response = None
    with open('_request', 'r') as file:
        calc = file.read()

# calc = "280,340,+"

    if calc:
        with open('_request', 'w') as file:
            file.write('')
        if calc[-1] == '+':
            response = add(calc)
        elif calc[-1] == '-':
            response = sub(calc)
        elif calc[-1] == '*':
            response = mult(calc)
        elif calc[-1] == '/':
            response = div(calc)

        with open('_response', 'w') as file:
            file.write(f"{response}")






