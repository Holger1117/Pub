import secrets

class rand:
    def __init__(self, modulus=10000, max_attempts=100, win_streak=95):
        self.key = self.generate_key()
        self.modulus = modulus
        self.max_attempts = max_attempts
        self.win_streak = win_streak
        self.sequence = []
        self.current_attempts = 0
        self.streak = 0
    
    def generate_key(self):
        key = ()
        for i in range(4):
            key += (secrets.randbelow(1000),)
        return key
        
    def generate_sequence(self, length):
        # Generate the sequence deterministically
        a, b, c, d = self.key
        seq = [(a + b * c) % self.modulus, (b + c * d) % self.modulus]
        
        for i in range(2, length):
            next_num = (a * seq[i - 1] + b * seq[i - 2] + c * (i + 1)**2 + d) % self.modulus
            seq.append(next_num)
        
        self.sequence = seq
        return seq

    def play(self):
        # Generate a long enough sequence for the game
        self.generate_sequence(self.max_attempts + self.win_streak)
        
        print("Guess the random numbers!")
        while self.current_attempts < self.max_attempts:
            correct_number = self.sequence[self.current_attempts]
            while 1:
                try:
                    guess = int(input(f"Attempt {self.current_attempts + 1}: "))
                    break
                except:
                    print("Please answer with a number!")
            
            if guess == correct_number:
                self.streak += 1
                print(f"Correct! Current streak: {self.streak}")
                if self.streak >= self.win_streak:
                    print("Congratulations! You guessed 95 in a row. Here's the flag: flag{r4nd0m_4n41y515_f7w_19fc4b28a6}")
                    break
            else:
                print(f"Wrong, the number was: {correct_number}\nTry again!")
                self.streak = 0
            
            self.current_attempts += 1
        
        if self.current_attempts >= self.max_attempts and self.streak < self.win_streak:
            print("Game over! Better luck next time.")

RRC = rand(4294967294)
RRC.play()
