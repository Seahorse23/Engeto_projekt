# project_1.py: prvni projekt do Engeto Online Python Akademie
# author: Patrik Perutka
# email: patrino19@seznam.cz
# discord: patrik_44080


# registered users
logins = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# login process
user = input("username: ")
password = input("password: ")

print("-" * 40)

for klic, hodnota in logins.items():     # goes through the dictionary and searches for a known combo of username+password
    if klic == user and password == hodnota:
        print(f"Welcome to the app, {user}.\nWe have 3 texts to be analyzed.")
        break
else:       
    print("Unregistered user, terminating the program...")
    quit()

print("-" * 40)

# texts to analyze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# user's choice of text 
user_choice = (input("Enter a number between 1 and 3: "))
if not user_choice.isdigit():
    print("Invalid input - not a number. Terminating the program...")
    quit()
elif int(user_choice) not in range(1,4):
    print("Invalid input - not a number between 1 and 3. Terminating the program...")
    quit()
else:
    chosen_text = TEXTS[int(user_choice) - 1]

# total word count, removing periods and commas for easier manipulation, mainly for the final graph
chosen_text = chosen_text.replace(".", " ").replace(",", " ")
print(f"There are {(len(chosen_text.split()))} words in the selected text.")

# word & num types 
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
num_strings = 0 
num_sum = 0 

for word in chosen_text.split():
    if word.istitle():
        titlecase_words += 1
    if word.isupper() and word.isalpha():
        uppercase_words += 1
    if word.islower():
        lowercase_words += 1
    if word.isdecimal():
        num_strings += 1
        num_sum += int(word)

print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {num_strings} numeric strings.")
print(f"The sum of all the numbers is {num_sum}.")

print("-" * 40)

# word length graph
print((f"{'LEN':<4}|{'OCCURRENCES':<13}|{'NR.':<2}"))
delkyslov = list()
for word in chosen_text.split():
    wordlength = len(word)
    delkyslov.append(wordlength)

for index in range(1,20):
    if delkyslov.count(index) != 0:
        print(f"{index:<4}|{('*' * delkyslov.count(index)):<13}|{delkyslov.count(index):<2}")
        