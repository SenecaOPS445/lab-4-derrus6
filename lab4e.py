#!/usr/bin/env python3
# Author ID: drussell6

def is_digits(sobj):
    digits = "0123456789"
    isDigit = True

    for digit in sobj:
        if digit in digits:
            isDigit = True
        else:
            isDigit = False
            return isDigit
    
    return isDigit

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')