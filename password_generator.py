import string
import random
letters = list(string.ascii_letters)
digits = list(string.digits)
spec_char = list("!@#$%^&*()_")
char = list(string.ascii_letters + string.digits + "!@#$%^&*()_")

def generate():
         lenght = None
         letter_count = None
         spec_char_count = None
         digit_count = None
         while lenght is None and letter_count is None and spec_char_count is None and digit_count is None:
                  lenght_input = input("Enter lenght of your password: ")
                  letter_count_input = input ("Enter letter count: ")
                  spec_char_count_input = input("Enter special character count: ")
                  digits_count_input = input("Enter digit count: ")

                  try:
                           lenght = int(lenght_input)
                           letter_count = int(letter_count_input)
                           spec_char_count = int(spec_char_count_input)
                           digit_count = int(digits_count_input)
                  except ValueError:
                           print("Wrong input! You must enter digit!")

         random.shuffle(char)
         char_lenght = letter_count + spec_char_count + digit_count
         password = [] 
         print(letter_count)
         for i in range (letter_count):
                  password.append(random.choice(letters))
         for i in range (spec_char_count):
                  password.append(random.choice(spec_char))  
         for i in range (digit_count):
                  password.append(random.choice(digits)) 
         random.shuffle(password)
         if lenght > char_lenght:
                  random.shuffle(char)
                  for i in range (lenght - char_lenght):
                           password.append(random.choice(char))
         random.shuffle(password)
         print("".join(password))

generate()
