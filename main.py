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
password=""
for l in range(1,nr_letters+1):
  letter_place = random.randint(0,len(letters)-1)
  password+=letters[letter_place]

for s in range(1,nr_symbols+1):
  symbol_place = random.randint(0,len(symbols)-1)
  password+=symbols[symbol_place]

for n in range(1,nr_numbers+1):
  number_place = random.randint(0,len(numbers)-1)
  password+=numbers[number_place]

print(password)
print("****************************")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password =""

total_char = nr_letters + nr_numbers + nr_symbols
letter_place=0
letterC=1
symbolC=1
numberC=1

ch = 1
while ch <= total_char:
  #print("char" + str(ch))
  what_will_it_be = random.randint(1,3) # 1 for Letter, 2 for  symbol, 3 for numbers
  #print("what_will_it_be= " + str(what_will_it_be))
  
  if what_will_it_be == 1 and letterC <= nr_letters:
    #input("le#"+str(letterC))
    letter_place = random.randint(0,len(letters)-1)
    password+=letters[letter_place]
    #input(password)
    letterC += 1
    ch+=1
    # print("CharnowLET"+str(ch))
    

  elif what_will_it_be == 2 and symbolC <= nr_symbols:
    #input("sy#"+str(symbolC))
    letter_place = random.randint(0,len(symbols)-1)
    password+=symbols[letter_place]
    #input(password)
    symbolC += 1
    ch+=1
    #print("CharnowSYM"+str(ch))

  elif what_will_it_be == 3 and numberC <= nr_numbers:
    #input("nu#"+str(numberC))
    letter_place = random.randint(0,len(numbers)-1)
    password+=numbers[letter_place]
    #input(password)
    numberC += 1
    ch+=1
    #print("CharnowNUM"+str(ch))
  



print(password)
  
