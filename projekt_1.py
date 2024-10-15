"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martina Kudelova
email: marti.kudelova@gmail.com
discord: martina_44769
"""
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }
oddelovac = "-" * 40
user = input("username:")
password = input("password:")
if user in registered_users.keys() and registered_users.get(user) == password:
    print(oddelovac, "\nWelcome to the app,",
          user,"\nWe have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    exit()
TEXTS = ['''
"Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley." ''',
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
print(oddelovac)
text = input("Enter a number btw. 1 and 3 to select: ")
if text.isdigit() == False or int(text) not in (1,2,3):
    print("Wrong number of text, terminating the program")
    exit()
print(oddelovac)
words = TEXTS[int(text)-1].split()
word_count = len(words)
print("There are", word_count, "words in the selected text.")
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
number_count = 0
number_sum = 0
for word in words:
    if word.istitle():
        titlecase_count += 1
    elif word.isupper() and word.isalpha():
        uppercase_count += 1
    elif word.islower():
        lowercase_count += 1
    elif word.isnumeric():
        number_count += 1
        number_sum = number_sum + int(word)
print("There are", titlecase_count, "titlecase words.") 
print("There are", uppercase_count, "uppercase words.")  
print("There are", lowercase_count, "lowercase words.")
print("There are", number_count, "numeric strings.")
print("The sum of all the numbers", number_sum)
print(oddelovac)
print("LEN|    OCCURENCES    |NR.")
print(oddelovac)
len1 = len2 = len3 = len4 = len5 = len6 = len7 = len8 = len9 = len10 = len11 = 0 #sice 80 znaků, ale přijde mi to nejpraktičtější
for word in words:
    clean_word = (
    word.replace('"', '')
    .replace(',', '')
    .replace('.', '')
    .replace("'", '')
)
    length = len(clean_word)
    if length == 1:
        len1 += 1
    elif length == 2:
        len2 += 1
    elif length == 3:
        len3 += 1
    elif length == 4:
        len4 += 1
    elif length == 5:
        len5 += 1
    elif length == 6:
        len6 += 1
    elif length == 7:
        len7 += 1
    elif length == 8:
        len8 += 1
    elif length == 9:
        len9 += 1
    elif length == 10:
        len10 += 1
    elif length == 11:
        len11 += 1
print(f"{1:>3}|{('*' * len1):<18}|{len1}")
print(f"{2:>3}|{('*' * len2):<18}|{len2}")
print(f"{3:>3}|{('*' * len3):<18}|{len3}")
print(f"{4:>3}|{('*' * len4):<18}|{len4}")
print(f"{5:>3}|{('*' * len5):<18}|{len5}")
print(f"{6:>3}|{('*' * len6):<18}|{len6}")
print(f"{7:>3}|{('*' * len7):<18}|{len7}")
print(f"{8:>3}|{('*' * len8):<18}|{len8}")
print(f"{9:>3}|{('*' * len9):<18}|{len9}")
print(f"{10:>3}|{('*' * len10):<18}|{len10}")
print(f"{11:>3}|{('*' * len11):<18}|{len11}")