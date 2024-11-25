import random, time, os

def first():
    random.seed(time.time())
    os.system("cls")
    print("Beat me in a guessing game! You got 1000 tries, if you guess the number i am thinking of ONCE, you win!\nHint: The number is between 0 and 200")
    for i in range(1000):
        number = random.randint(0, 200)
        while 1:
            try:
                guess = int(input("Guess the number i am thinking of!\n> "))
                break
            except:
                print("Please type a number!")
                continue
        if guess == number:
            print("Congratulations! Now we move on to the next round!")
            time.sleep(2)
            os.system("cls")
            second()
            break
        else:
            print("Wrong, the number was: ", number)
            os.system("cls")

def second():
    times_guessed = 0
    random.seed(time.time())
    print("Ok you beat me the first time, but that was easy!")
    print("Now we make it harder. You got 1000 tries again, but this time you have to guess the number correctly 300 times in a row, and the number is between 0 and 4294967294!\n")
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
            if times_guessed == 300:
                print("Wow you are really good at guessing, here is your flag: flag{r4nd0m3n355_1n_py7h0n_5uck5_16c8b1fe95}")
                quit()
            print(f"Right! Just {300 - times_guessed} times left!")
        else:
            print("Wrong, the number was: ", number)
            os.system("cls")

first()