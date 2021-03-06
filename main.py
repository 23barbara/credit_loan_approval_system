'''
the main function will apply the logistic regression built to client data.
reads input data from a user and returns the result
based on predicted value
'''

from classification_system import *

if __name__ == '__main__':
    # first get data from user
    print("Enter client data.")
    print("Account balance:")
    print("[1] no running account [2] no balance [3] 0 <= ... < 200 DM [4] ... >= 200 DM")
    balance = int(input())

    print("Duration of credit: ")
    print("Enter a value from 1 to 10 based on categories.")
    duration = int(input())

    print("Current status of previous credit: ")
    print("[1] problematic [2] no previous credits [3] no problems"
          "[4] paid back previous credits [0] hesitant payment of previous credits")
    payment_status = int(input())

    # save data
    client = tuple((balance, duration, payment_status))

    print('Result: ' + print_result(client))