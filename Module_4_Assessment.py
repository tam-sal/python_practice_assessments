# -*- coding: utf-8 -*-

'''1 -Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.'''


class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price

testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)

'''2 -Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)'''

class AppleBasket:
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity
    
    def increase(self):
        self.apple_quantity += 1
        
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)
    
five_red_apples = AppleBasket("red" , 5)
print(five_red_apples)
five_red_apples.increase()
print(five_red_apples)

'''3 -Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1.'''

class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt
        
    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)
        
        
t1 = BankAccount("Bob", 100)
print(t1)

#### Stanalone Project
'''4 -The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.

Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.

For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!". Create an instance of this class with the name as "Belle". Assign this instance to the variable p1.'''

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12


    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)
p1 = Grass_Pokemon("Belle")
print(p1)

'''Modify the Grass_Pokemon subclass so that the attack strength for Grass_Pokemon instances does not change until they reach level 10. At level 10 and up, their attack strength should increase by the attack_boost amount when they are trained.

To test, create an instance of the class with the name as "Bulby". Assign the instance to the variable p2. Create another instance of the Grass_Pokemon class with the name set to "Pika" and assign that instance to the variable p3. Then, use Grass_Pokemon methods to train the p3 Grass_Pokemon instance until it reaches at least level 10.'''

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def attack_up(self):
        if self.level >= 10:
            self.attack = self.attack + self.attack_boost
            return self.attack
        return self.attack
p2 = Grass_Pokemon("Bulby")

p3 = Grass_Pokemon("Pika")
for i in range(10):
    p3.train()
p3.attack_up()

'''Along with the Pokemon parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it opponent. It should return which type of pokemon the current type is weak and strong against, as a tuple.

Grass is weak against Fire and strong against Water

Ghost is weak against Dark and strong against Psychic

Fire is weak against Water and strong against Grass

Flying is weak against Electric and strong against Fighting

For example, if the p_type of the subclass is 'Grass', .opponent() should return the tuple ('Fire', 'Water')'''

class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10
        
    def opponent(self):
        if self.p_type == 'Grass':
            return ('Fire', 'Water')
        elif self.p_type == 'Ghost':
            return ('Dark', 'Psychic')
        elif self.p_type == 'Fire':
            return ('Water','Grass')
        else:
            return ('Electric', 'Fighting')
        
    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

class Flying_Pokemon(Pokemon):
    p_type = "Flying"

'''5 -Write code so that the buggy code provided works using a try/except. When the codes does not work in the try, have it append to the list attempt the string “Error”.'''
full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        a = elem[1]
        attempt.append(a)
    except:
        attempt.append("Error")

'''6 -The following code tries to append the third element of each list in conts to the new list third_countries. Currently, the code does not work. Add a try/except clause so the code runs without errors, and the string ‘Continent does not have 3 countries’ is appended to countries instead of producing an error.'''

conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'], ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'], ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

a = "Continent does not have 3 countries"
third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except:
        third_countries.append(a)

'''7 -The buggy code below prints out the value of the sport in the list sport. Use try/except so that the code will run properly. If the sport is not in the dictionary, ppl_play, add it in with the value of 1.'''

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except:
        ppl_play.update({x:1})


'''8 -Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes. If the key is not there, initialize it in the dictionary and set the value to zero.'''

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except:
        diction.update({'Puppies' : 0})

print("Total number of puppies:", total)

################ Standalone Project ##################
'''9 -This project will take you through the process of implementing a simplified version of the game Wheel of Fortune. Here are the rules of our game:

There are num_human human players and num_computer computer players.
Every player has some amount of money ($0 at the start of the game)

Every player has a set of prizes (none at the start of the game)

The goal is to guess a phrase within a category. For example:
Category: Artist & Song

Phrase: Whitney Houston’s I Will Always Love You

Players see the category and an obscured version of the phrase where every alphanumeric character in the phrase starts out as hidden (using underscores: _):
Category: Artist & Song

Phrase: _______ _______'_ _ ____ ______ ____ ___

Note that case (capitalization) does not matter

During their turn, every player spins the wheel to determine a prize amount and:
If the wheel lands on a cash square, players may do one of three actions:
Guess any letter that hasn’t been guessed by typing a letter (a-z)
Vowels (a, e, i, o, u) cost $250 to guess and can’t be guessed if the player doesn’t have enough money. All other letters are “free” to guess

The player can guess any letter that hasn’t been guessed and gets that cash amount for every time that letter appears in the phrase

If there is a prize, the user also gets that prize (in addition to any prizes they already had)

If the letter does appear in the phrase, the user keeps their turn. Otherwise, it’s the next player’s turn

Example: The user lands on $500 and guesses ‘W’
There are three W’s in the phrase, so the player wins $1500

Guess the complete phrase by typing a phrase (anything over one character that isn’t ‘pass’)
If they are correct, they win the game

If they are incorrect, it is the next player’s turn

Pass their turn by entering 'pass'

If the wheel lands on “lose a turn”, the player loses their turn and the game moves on to the next player

If the wheel lands on “bankrupt”, the player loses their turn and loses their money but they keep all of the prizes they have won so far.

The game continues until the entire phrase is revealed (or one player guesses the complete phrase)

—

First, let’s learn about a few functions and methods that we’ll use along the way to do this project. There are no questions to answer in the next four active code windows. They are just here to introduce you to some functions and methods that you may not be aware of. The active code window that starts with “Part A” is where you are first asked to complete code.

—

The time.sleep(s) function (from the time module) delays execution of the next line of code for s seconds. You’ll find that we can build a little suspense during gameplay with some well-placed delays. The game can also be easier for users to understand if not everything happens instantly.'''

import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

category, phrase = getRandomCategoryAndPhrase()

guessed = []
for x in range(random.randint(10, 20)):
    randomLetter = random.choice(LETTERS)
    if randomLetter not in guessed:
        guessed.append(randomLetter)

print("getRandomCategoryAndPhrase()\n -> ('{}', '{}')".format(category, phrase))

print("\n{}\n".format("-"*5))

print("obscurePhrase('{}', [{}])\n -> {}".format(phrase, ', '.join(["'{}'".format(c) for c in guessed]), obscurePhrase(phrase, guessed)))

print("\n{}\n".format("-"*5))

obscured_phrase = obscurePhrase(phrase, guessed)
print("showBoard('{}', '{}', [{}])\n -> {}".format(phrase, obscured_phrase, ','.join(["'{}'".format(c) for c in guessed]), showBoard(phrase, obscured_phrase, guessed)))

print("\n{}\n".format("-"*5))

num_times_to_spin = random.randint(2, 5)
print('Spinning the wheel {} times (normally this would just be done once per turn)'.format(num_times_to_spin))

for x in range(num_times_to_spin):
    print("\n{}\n".format("-"*2))
    print("spinWheel()")
    print(spinWheel())


print("\n{}\n".format("-"*5))

print("In 2 seconds, will run getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10)")

time.sleep(2)

print(getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10))

'''Part A: WOFPlayer

We’re going to start by defining a class to represent a Wheel of Fortune player, called WOFPlayer. Every instance of WOFPlayer has three instance variables:

.name: The name of the player (should be passed into the constructor)

.prizeMoney: The amount of prize money for this player (an integer, initialized to 0)

.prizes: The prizes this player has won so far (a list, initialized to [])

Of these instance variables, only name should be passed into the constructor.

It should also have the following methods (note: we will exclude self in our descriptions):

.addMoney(amt): Add amt to self.prizeMoney

.goBankrupt(): Set self.prizeMoney to 0

.addPrize(prize): Append prize to self.prizes

.__str__(): Returns the player’s name and prize money in the following format:
Steve ($1800) (for a player with instance variables .name == 'Steve' and prizeMoney == 1800)

Part B: WOFHumanPlayer

Next, we’re going to define a class named WOFHumanPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a human player. In addition to having all of the instance variables and methods that WOFPlayer has, WOFHumanPlayer should have an additional method:

.getMove(category, obscuredPhrase, guessed): Should ask the user to enter a move (using input()) and return whatever string they entered.
.getMove()’s prompt should be:

{name} has ${prizeMoney}

Category: {category}
Phrase:  {obscured_phrase}
Guessed: {guessed}

Guess a letter, phrase, or type 'exit' or 'pass':
For example:

Steve has $200

Category: Places
Phrase: _L___ER N____N_L P_RK
Guessed: B, E, K, L, N, P, R, X, Z

Guess a letter, phrase, or type 'exit' or 'pass':
The user can then enter:

'exit' to exit the game

'pass' to skip their turn

a single character to guess that letter

a complete phrase (a multi-character phrase other than 'exit' or 'pass') to guess that phrase

Note that .getMove() does not need to enforce anything about the user’s input; that will be done via the game logic that we define in the next ActiveCode window.

Part C: WOFComputerPlayer

Finally, we’re going to define a class named WOFComputerPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a computer player.

Every computer player will have a difficulty instance variable. Players with a higher difficulty generally play “better”. There are many ways to implement this. We’ll do the following:

If there aren’t any possible letters to choose (for example: if the last character is a vowel but this player doesn’t have enough to guess a vowel), we’ll 'pass'

Otherwise, semi-randomly decide whether to make a “good” move or a “bad” move on a given turn (a higher difficulty should make it more likely for the player to make a “good” move)
To make a “bad” move, we’ll randomly decide on a possible letter.

To make a “good” move, we’ll choose a letter according to their overall frequency in the English language.

In addition to having all of the instance variables and methods that WOFPlayer has, WOFComputerPlayer should have:

Class variable

.SORTED_FREQUENCIES: Should be set to 'ZQXJKVBPYGFWMUCLDRHSNIOATE', which is a list of English characters sorted from least frequent ('Z') to most frequent ('E'). We’ll use this when trying to make a “good” move.

Additional Instance variable

.difficulty: The level of difficulty for this computer (should be passed as the second argument into the constructor after .name)

Methods

.smartCoinFlip(): This method will help us decide semi-randomly whether to make a “good” or “bad” move. A higher difficulty should make us more likely to make a “good” move. Implement this by choosing a random number between 1 and 10 using random.randint(1, 10) (see above) and returning False if that random number is greater than self.difficulty. If the random number is less than or equal to self.difficulty, return True.

.getPossibleLetters(guessed): This method should return a list of letters that can be guessed.
These should be characters that are in LETTERS ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') but not in the guessed parameter.

Additionally, if this player doesn’t have enough prize money to guess a vowel (variable VOWEL_COST set to 250), then vowels (variable VOWELS set to 'AEIOU') should not be included

.getMove(category, obscuredPhrase, guessed): Should return a valid move.
Use the .getPossibleLetters(guessed) method described above.

If there aren’t any letters that can be guessed (this can happen if the only letters left to guess are vowels and the player doesn’t have enough for vowels), return 'pass'

Use the .smartCoinFlip() method to decide whether to make a “good” or a “bad” move
If making a “good” move (.smartCoinFlip() returns True), then return the most frequent (highest index in .SORTED_FREQUENCIES) possible character

If making a “bad” move (.smartCoinFlip() returns False), then return a random character from the set of possible characters (use random.choice())'''

import json
import random
import time

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        WOFPlayer.__init__(self, name)
    
    def getMove(self, category, obsecuredPhrase, guessed):
        print("{} has ${}".format(self.name, self.prizeMoney))
        print("\n\n")
        print("Category: {}".format(category))
        print("Phrase: {}".format(obsecuredPhrase))
        print("Guessed: {}".format(guessed))
        print("\n\n")
        human_input = str(input("Guess a letter, phrase, or type 'exit' or 'pass': "))
        return human_input


# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty
    
    def smartCoinFlip(self):
        threshold = random.randint(1, 10)
        if threshold > self.difficulty:
            return False
        return True
    
    def getPossibleLetters(self, guessed):
        guessables = []
        for letter in LETTERS:
            if letter not in guessed and letter in VOWELS and self.prizeMoney > VOWEL_COST:
                guessables.append(letter)
            elif letter not in guessed and letter not in VOWELS:
                guessables.append(letter)
        return guessables
    
    def getMove(self, category, obsecuredPhrase, guessed):
        guessables = self.getPossibleLetters(guessed)
        updated_sorted_freq = []
        for char in self.SORTED_FREQUENCIES:
            if char in guessables:
                updated_sorted_freq.append(char)
        coinFResult = self.smartCoinFlip()
        if len(guessables) == 0:
            return 'pass'
        else:
            if coinFResult:
                return updated_sorted_freq[-1]
            else:
                return random.choice(updated_sorted_freq)
##### Complete
# PASTE YOUR WOFPlayer CLASS (from part A) HERE
import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250
###                                  Part1
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

# PASTE YOUR WOFHumanPlayer CLASS (from part B) HERE

class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        WOFPlayer.__init__(self, name)
    
    def getMove(self, category, obsecuredPhrase, guessed):
        print("{} has ${}".format(self.name, self.prizeMoney))
        print("\n\n")
        print("Category: {}".format(category))
        print("Phrase: {}".format(obsecuredPhrase))
        print("Guessed: {}".format(guessed))
        print("\n\n")
        human_input = str(input("Guess a letter, phrase, or type 'exit' or 'pass': "))
        return human_input
# PASTE YOUR WOFComputerPlayer CLASS (from part C) HERE
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty
    
    def smartCoinFlip(self):
        threshold = random.randint(1, 10)
        if threshold > self.difficulty:
            return False
        return True
    
    def getPossibleLetters(self, guessed):
        guessables = []
        for letter in LETTERS:
            if letter not in guessed and letter in VOWELS and self.prizeMoney > VOWEL_COST:
                guessables.append(letter)
            elif letter not in guessed and letter not in VOWELS:
                guessables.append(letter)
        return guessables
    
    def getMove(self, category, obsecuredPhrase, guessed):
        guessables = self.getPossibleLetters(guessed)
        updated_sorted_freq = []
        for char in self.SORTED_FREQUENCIES:
            if char in guessables:
                updated_sorted_freq.append(char)
        coinFResult = self.smartCoinFlip()
        if len(guessables) == 0:
            return 'pass'
        else:
            if coinFResult:
                return updated_sorted_freq[-1]
            else:
                return random.choice(updated_sorted_freq)

import sys
sys.setExecutionLimit(600000) # let this take up to 10 minutes

import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

# GAME LOGIC CODE
print('='*15)
print('WHEEL OF PYTHON')
print('='*15)
print('')

num_human = getNumberBetween('How many human players?', 0, 10)

# Create the human player instances
human_players = [WOFHumanPlayer(input('Enter the name for human player #{}'.format(i+1))) for i in range(num_human)]

num_computer = getNumberBetween('How many computer players?', 0, 10)

# If there are computer players, ask how difficult they should be
if num_computer >= 1:
    difficulty = getNumberBetween('What difficulty for the computers? (1-10)', 1, 10)

# Create the computer player instances
computer_players = [WOFComputerPlayer('Computer {}'.format(i+1), difficulty) for i in range(num_computer)]

players = human_players + computer_players

# No players, no game :(
if len(players) == 0:
    print('We need players to play!')
    raise Exception('Not enough players')

# category and phrase are strings.
category, phrase = getRandomCategoryAndPhrase()
# guessed is a list of the letters that have been guessed
guessed = []

# playerIndex keeps track of the index (0 to len(players)-1) of the player whose turn it is
playerIndex = 0

# will be set to the player instance when/if someone wins
winner = False

def requestPlayerMove(player, category, guessed):
    while True: # we're going to keep asking the player for a move until they give a valid one
        time.sleep(0.1) # added so that any feedback is printed out before the next prompt

        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper() # convert whatever the player entered to UPPERCASE
        if move == 'EXIT' or move == 'PASS':
            return move
        elif len(move) == 1: # they guessed a character
            if move not in LETTERS: # the user entered an invalid letter (such as @, #, or $)
                print('Guesses should be letters. Try again.')
                continue
            elif move in guessed: # this letter has already been guessed
                print('{} has already been guessed. Try again.'.format(move))
                continue
            elif move in VOWELS and player.prizeMoney < VOWEL_COST: # if it's a vowel, we need to be sure the player has enough
                    print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                    continue
            else:
                return move
        else: # they guessed the phrase
            return move


while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()

    print('')
    print('-'*15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print('')
    print('{} spins...'.format(player.name))
    time.sleep(2) # pause for dramatic effect!
    print('{}!'.format(wheelPrize['text']))
    time.sleep(1) # pause again for more dramatic effect!

    if wheelPrize['type'] == 'bankrupt':
        player.goBankrupt()
    elif wheelPrize['type'] == 'loseturn':
        pass # do nothing; just move on to the next player
    elif wheelPrize['type'] == 'cash':
        move = requestPlayerMove(player, category, guessed)
        if move == 'EXIT': # leave the game
            print('Until next time!')
            break
        elif move == 'PASS': # will just move on to next player
            print('{} passes'.format(player.name))
        elif len(move) == 1: # they guessed a letter
            guessed.append(move)

            print('{} guesses "{}"'.format(player.name, move))

            if move in VOWELS:
                player.prizeMoney -= VOWEL_COST

            count = phrase.count(move) # returns an integer with how many times this letter appears
            if count > 0:
                if count == 1:
                    print("There is one {}".format(move))
                else:
                    print("There are {} {}'s".format(count, move))

                # Give them the money and the prizes
                player.addMoney(count * wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                # all of the letters have been guessed
                if obscurePhrase(phrase, guessed) == phrase:
                    winner = player
                    break

                continue # this player gets to go again

            elif count == 0:
                print("There is no {}".format(move))
        else: # they guessed the whole phrase
            if move == phrase: # they guessed the full phrase correctly
                winner = player

                # Give them the money and the prizes
                player.addMoney(wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                break
            else:
                print('{} was not the phrase'.format(move))

    # Move on to the next player (or go back to player[0] if we reached the end)
    playerIndex = (playerIndex + 1) % len(players)

if winner:
    # In your head, you should hear this as being announced by a game show host
    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
else:
    print('Nobody won. The phrase was {}'.format(phrase))
