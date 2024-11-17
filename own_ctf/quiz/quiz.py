#moduler som behövs
from random import randint, choice
from time import sleep, time
from os import system
import string
import sys
import threading
from datetime import datetime, timedelta

#globala variabler
finalsum = 0
finalfactor = 1
randomint = 0

#funktion för om svaret är fel
def bye():
    print("Sorry, wrong... try again next time, bye!\n")
    quit()

#funktion för om spelaren fick slut på tid
def bye_timeout():
    print("Sorry, you ran out of time... too bad\n")
    quit()


#funktion som genererar en slumpmässig sträng mellan 10-20 karaktärer alternerande mellan siffror och bokstäver
def randstr():
    length = randint(10, 20)
    characters = []


    for i in range(length):
        if i % 3 == 0:
            characters.append(choice(string.ascii_lowercase))

        elif i % 3 == 1:
            characters.append(choice(string.ascii_uppercase))

        else:
            characters.append(choice(string.digits))

    random_string = ''.join(characters)
    return random_string


#funktion som skapar en delay på en input på "timeout" sekunder och quittar om tiden är ute
def input_time(prompt, timeout):
    print(prompt)
    sys.stdout.flush()
    input_data = []

    #Funktion för att få input
    def get_input():
        input_data.append(input())

    #Starta en separat tråd som tar emot inputten
    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()


    #Vänta på att tråden slutförs eller att tiden går ut
    thread.join(timeout)

    #Om tråden fortfarande finns så betyder det att tiden gått ut och spelaren har fortfarande inte svarat
    if thread.is_alive():
        bye_timeout()

    else:
        return input_data[0]


#Funktion för att kolla om ett nummer är primtal

def is_prime(num):
    if num <= 1:
        return False

    elif num <= 3:
        return True

    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5

    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


#Funktion för att räkna ut de n'te primtalet
def nth_prime(n):
    if n == 1:
        return 2

    count = 1
    num = 1

    while count < n:
        num += 2

        if is_prime(num):
            count += 1
    return num

#Funktion för att räkna ut det n'te nummret i fibonaccis talföljd
def fibonacci(n):
    if n <= 0:
        return "Invalid input"

    elif n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[-1] + fib_list[-2])

        return fib_list[-1]

   

#Funktion för att räkna antalet söndagar mellan två datum

def count_sundays(start_date, end_date):
    count = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() == 6:  # Sunday
            count += 1

        current_date += timedelta(days=1)
    return count


#Första frågan
def one():
    global finalsum
    answer = input("Ok, for question one, what is 12 + 48?\n")
    correct = 12 + 48
    finalsum = finalsum + correct #Adderar svaret till den slutgiltiga summan

    try:
        if int(answer) == correct:
            print("Good job! This was easy, next question...\n")
            sleep(2)
            system('cls')

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()


#Andra frågan
def two():
    global finalsum
    answer = input("For question 2, what is 117 * 534?\n")
    correct = 117 * 534
    finalsum = finalsum + correct

    try:
        if int(answer) == correct:
            print("Good job! This was easy, next question...\n")
            sleep(2)
            system('cls')

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()

#Tredje frågan
def three():
    global finalsum
    answer = input("For question 3, what is ∛315821241?\n")
    correct = round(315821241 ** (1/3)) #Rundar upp det till närmsta heltal då svaret annars blir 680.999999...
    finalsum = finalsum + correct

    try:
        if int(answer) == correct:
            print("Good job! This was easy, next question...\n")
            sleep(2)
            system('cls')

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()

#Fjärde frågan
def four():
    global finalsum
    global finalfactor
    global randomint
    randomint = randint(100000, 999999) #random tal mellan hundra tusen och en miljon
    answer = input_time(f"For question 4, what is the digit sum of {randomint}? You have 1 second to answer...\n", 1)
    correct = sum(int(digit) for digit in str(randomint))
    finalsum = finalsum + correct
    finalfactor = finalfactor * correct #multiplicerar till sjunde frågan

    try:
        if int(answer) == correct:
            print("Good job! This was easy, next question...\n")
            sleep(2)
            system('cls')

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()

#Femte frågan
def five():
    global finalsum
    global finalfactor
    global randomint
    answer = input(f"For question 5, what was the number generated in the last question?\n")
    correct = randomint
    finalsum = finalsum + correct
    finalfactor = finalfactor * correct
    try:
        if int(answer) == correct:
            print("Good job! This was easy, next question...\n")
            sleep(2)
            system('cls')

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()

#Sjätte frågan
def six():
    global finalsum
    global finalfactor
    random_string = randstr() #Generar en random sträng med stora och små bokstäver samt siffror
    answer = input(f"For question 6, what is the number formed by concatenating all the digits in the following string: {random_string}?\n")
    correct = int(''.join([char for char in random_string if char.isdigit()])) #lägger ihop alla siffror som finns i stränge med for-loop
    finalsum = finalsum + correct
    finalfactor = finalfactor * correct

    try:
        if int(answer) == correct:
            print("Good job! This was easy, next question...\n")
            sleep(2)
            system('cls')

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()

#Sjunde frågan
def seven():

    global finalsum
    global finalfactor
    answer = input_time("For question 7, what is the factor of the last three answers? You have 1 seconds to answer!\n", 1)
    correct = finalfactor
    finalsum = finalsum + correct

    try:
        if int(answer) == correct:
            print("Good job! This was easy, next question...\n")
            sleep(2)
            system('cls')

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()

#Åttonde frågan

def eight():
    global finalsum
    prime = randint(100, 10000) #Generar ett random tal mellan hundra och tio tusen
    primeanswer = nth_prime(prime) #kollar vilket primtalet är som generats
    answer = input_time(f"For question 8, what is the sum of all the previous answers plus the {prime}'th prime number? You have 1 second to answer\n", 1)
    print(primeanswer)
    correct = finalsum + primeanswer

    try:
        if int(answer) == correct:
            print("Good job! This was easy, next question...\n")
            sleep(2)
            system('cls')

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()

#Nionde frågan

def nine():
    rand = randint(20, 30) #Genererar ett random tal mellan 20 och 30
    fib_number = fibonacci(rand) #Kollan vilket nummer i fibonacci sekvensen som ligger på den platsen som genererats
    start_date = datetime(2000, 1, 1) #sätter startdatument till 1 jan 2020
    end_date = datetime.now() #Sätter sluttiden till nu så den jämför med rätt datum

    random_date = datetime.fromordinal(randint(start_date.toordinal(), end_date.toordinal())) #Tar fram ett random datum från 1 jan 2020

    sundays_since_random_date = count_sundays(random_date, end_date) #räknar ut hur många söndagar som varit sedan det genererade datumet
    answer = input_time(f"For question 9, what is the {rand}'th number in the fibonacci sequence times the amount of sundays since {random_date.strftime('%Y-%m-%d')}? You have 1 second to answer\n", 1)
    correct = fib_number * sundays_since_random_date

    try:
        if int(answer) == correct:
            print("Good job! This was easy, here is the flag: ")

            with open("flag.txt", "r") as f:
                print(f.readlines()[0])

            sleep(2)

        else:
            bye()

    except:
        print("Please only answer with a number! try again next time\n")
        quit()


#Main, kör om man är redo, kör inte annars
system('cls')
print("Welcome to the math quiz! You will get a set of questions, and you should answer within a reasonable amount of time, good luck!\n")
answer = input("Are you ready?\n")

if answer.lower() == "yes":
    system('cls')
    print("Nice! Lets get going!\n")

elif answer.lower() == "no":
    print("Too bad, bye!\n")
    quit()

else:
    print("Please answer with yes or no next time!\n")
    quit()

one()
two()
three()
four()
five()
six()
seven()
eight()
nine()