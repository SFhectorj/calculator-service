import time
import os

REQUEST_FILE = "_request"
RESPONSE_FILE = "_response"

while True:
    expression = input("Enter calculation in Reverse Polish notation (ex: 5,5,+): ")


    parts = expression.split(',')
    if len(parts) != 3:
        print("Invalid format. Use: number, number, operator")
        continue

    # Clear previous response before sending request
    open(RESPONSE_FILE, "w").close()

    # Send request
    with open(REQUEST_FILE, "w") as f:
        f.write(expression)

    # Look for response from calculator_microservice.py
    while True:
        if os.path.exists(RESPONSE_FILE):
            with open(RESPONSE_FILE, "r") as f:
                response = f.read().strip()

            if response != "":
                break

        time.sleep(0.5)

    # Process response
    if response == "ERROR":
        print("ERROR: Please try again.")

    else:
        print(float(response))
    
    # Clear response file for the next request
    open(RESPONSE_FILE, "w").close()
