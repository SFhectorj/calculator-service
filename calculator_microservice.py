import os
import time

REQUEST_FILE = "_request"
RESPONSE_FILE = "_response"
LOG_FILE = "calc_log.txt"

def log(message):
    '''
    User Story 3: Logs User interaction
    Satisfies Reliability requirment
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

ops = { "+": add, "-": sub, "*": mult, "/": div}

print("Calulator microservice is running...")

