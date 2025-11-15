import os
import time

REQUEST_FILE = "_request"
RESPONSE_FILE = "_response"
LOG_FILE = "calc_log.txt"

def log(message):
    '''
    User Story 3: Logs User interaction
    Satisfies Reliability requirement
    '''
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def add(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b
def div(a, b):
    if b == 0:
        return "ERROR"
    return a / b

operator_bank = { "+": add, "-": sub, "*": mult, "/": div}

print("Calculator microservice is running...")

while True:
    if os.path.exists(REQUEST_FILE):
        with open(REQUEST_FILE, "r") as f:
            data = f.read().strip()

        if data:
            # Clear request to make sure it only gets processed once
            open(REQUEST_FILE, "w").close()
            # Parse data
            parts = data.split(",")

            # Returns error if incorrect format recieved
            if len(parts) != 3:
                result = "ERROR"
            else:
                num1, num2, operator = parts

                # Check if operator recieved is in operator_bank
                try:
                    a = float(num1)
                    b = float(num2)

                    if operator not in operator_bank:
                        result = "ERROR"
                    else:
                        # Calculate
                        result = operator_bank[operator](a, b)
                except:
                    result = "ERROR"
                
            # Log input and Return result
            log(f"INPUT: {data} OUTPUT: {result}")

            with open(RESPONSE_FILE, "w") as f:
                f.write(str(result))

    time.sleep(0.05)