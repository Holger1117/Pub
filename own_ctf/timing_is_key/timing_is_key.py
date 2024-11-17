import time
import sys
import random
import string

# The correct 10-digit PIN code
# CORRECT_PIN = str(random.randrange(1000000000, 9999999999))  # example PIN code

def generate_random_string(length):

    characters = string.ascii_letters + string.digits  # Combine lowercase, uppercase, and digits
    return ''.join(random.choices(characters, k=length))

CORRECT_PIN = generate_random_string(random.randint(5,21))
print("Welcome to PING! (PIN Guessinggame) You have 60 seconds to guess a PIN that is between 5-20 characters long and contains digits 0-9, charcters a-z and A-Z. Good luck!")

def check_pin(user_pin):
    # Check each digit one by one and return False immediately if there's a mismatch
    if len(user_pin) != len(CORRECT_PIN):
        return False
    
    for i in range(len(CORRECT_PIN)):
        if user_pin[i] != CORRECT_PIN[i]:
            return False
        # Introduce a small delay to simulate work for each character comparison
        time.sleep(0.005)
    return True

def main():
    start_time = time.time()  # Record the start time

    while True:
        # Check if 60 seconds have passed
        if time.time() - start_time >= 60:
            print("Time's up! Exiting the program.")
            sys.exit()  # Exit the program after 60 seconds

        # Prompt the user for the PIN
        user_pin = input("Enter the PIN code: ")
        if check_pin(user_pin):
            print("flag{S1d3_ch4nn3l5_4r3_fun_734bf1e9cba}")
            break  # Exit the loop if the correct PIN is entered
        else:
            print("Incorrect PIN, try again.")

if __name__ == "__main__":
    main()
