import time
import random

while True:
    decision = input("Do you want to generate a password? y/n ")
    if decision == 'y':
        length = int(input("Enter the length of password: "))
        print("Generating Password...")
        s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        p = ''
        for i in range(0, length, 1):
            p += s[random.randint(0, len(s))]
        time.sleep(3)
        print(p)
    else:
        break