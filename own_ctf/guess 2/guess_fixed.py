import time
import random
import os

times_guessed = 0
random.seed(time.time())
print("Ok you beat me the last time, but i hear you use some sort of randcracker? That wont work now baby!")
print("Now we make it harder. You got 1000 tries again, but this time you have to guess the number correctly 990 times in a row, and the number is between 0 and 4294967294 again! Good luck...\n")
for i in range(1000):
    number = random.getrandbits(32)
    while 1:
        try:
            guess = int(input("Guess the number i am thinking of!\n> "))
            break
        except:
            print("Please type a number!")
            continue
    if guess == number:
        times_guessed += 1
        if times_guessed == 990:
            print("Wow you are really good at guessing, here is your flag: flag{m4k3_y0ur_0wn_c0d3_70_5ucc33d_17bd0a53fc}")
            quit()
        print(f"Right! Just {990 - times_guessed} times left!")
        os.system("cls")
    else:
        print("Wrong, the number was: ", number)