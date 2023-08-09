#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Set variables to use 
count = 0
final_password = []
final_password_mixed = []
password_letters = []
password_number = []
password_symbol = []

#Loop each character append to array
for letter in letters:
  if nr_letters > 0 and count != nr_letters:
    count += 1
    random_letter = random.choice(letters)
    password_letters.append(random_letter)

# Reset count
count = 0

#Loop each character append to array
for number in numbers:
  if nr_numbers > 0 and count != nr_numbers:
    count += 1
    random_number = random.choice(numbers)
    password_number.append(random_number)

#Reset count
count = 0
#Loop each character append to array
for symbol in symbols:
  if nr_symbols > 0 and count != nr_symbols:
    count += 1
    random_symbol = random.choice(symbols)
    password_symbol.append(random_symbol)

final_password = password_letters + password_number + password_symbol
final_length = len(final_password)

count = 0
for item in final_password:
  if count <= final_length:
    random_choice = random.choice(final_password)
    final_password_mixed.append(random_choice)
    count += 1

# Join the characters together
generated_password = ''.join(final_password_mixed)
print(f"Here is the password: {generated_password}")

