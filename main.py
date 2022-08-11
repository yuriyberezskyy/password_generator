#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# generated_password = []

# while nr_letters:
#   random_letter_index = random.randint(0,len(letters)-1)
#   letter = letters[random_letter_index]
#   generated_password.append(letter)
#   nr_letters-=1


# while nr_symbols:
#   random_symbol_index = random.randint(0,len(symbols)-1)
#   symbol = symbols[random_symbol_index]
#   generated_password.append(symbol)
#   nr_symbols-=1


# while nr_numbers:
#   random_number_index = random.randint(0,len(numbers)-1)
#   number = numbers[random_number_index]
#   generated_password.append(number)
#   nr_numbers-=1

# new_password =''
# while len(generated_password) > 0:
#   random_element_index = random.randint(0,len(generated_password)-1)
#   el = generated_password.pop(random_element_index)
#   new_password+=el
  
password_list=[]

for char in range(1, nr_letters +1 ):
  password_list +=random.choice(letters)

for char in range(1,nr_symbols +1):
  password_list += random.choice(symbols)

for char in range(1,nr_numbers+1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)
password =''

for char in password_list:
  password += char

print(password)