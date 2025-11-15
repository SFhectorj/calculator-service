import time


while True:
    expression = input("Enter calculation in Reverse Polish with commas between each portion like 5,5,+:")

    parts = expression.split(',')


    with open('_request', 'w') as file:
        file.write(f'{parts[0]},{parts[1]},{parts[2]}')

    time.sleep(1)

    with open('_response', 'r') as file:
        response = file.read()

    if response == 'ERROR':
        print(response)
    else:
        response = float(response)
        print(response)
