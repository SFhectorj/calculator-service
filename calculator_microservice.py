import os
import time

REQUEST_FILE = "_request"                       # replace as needed
RESPONSE_FILE = "_response"                     # replace as needed
LOG_FILE = "calc_log.txt"



# logging history

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")



# calculation functions

def add(num1, num2): 
    return num1 + num2

def sub(num1, num2): 
    return num1 - num2

def mult(num1, num2): 
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "ERROR"
    return num1 / num2



operator_bank = { "+": add, "-": sub, "*": mult, "/": div}



# program

print("Calculator microservice is running...")

while True:
    if os.path.exists(REQUEST_FILE):
        with open(REQUEST_FILE, "r") as f:      # clear request to avoid being processed multiple times
            data = f.read().strip()

        if data: 
            open(REQUEST_FILE, "w").close()
            parts = data.split(",")

            if len(parts) != 3:                 # in case of improper format
                result = "ERROR"

            else:
                num1, num2, operator = parts    # check for valid operator

                try:
                    num1 = float(num1)
                    num2 = float(num2)

                    if operator not in operator_bank:
                        result = "ERROR"
                    else:
                        result = operator_bank[operator](num1, num2)

                except:
                    result = "ERROR"
                
            log(f"INPUT: {data} OUTPUT: {result}")

            with open(RESPONSE_FILE, "w") as f:
                f.write(str(result))

    time.sleep(0.5)