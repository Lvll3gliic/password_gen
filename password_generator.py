import string
import random
letters = list(string.ascii_letters)
digits = list(string.digits)
spec_char = list("!@#$%^&*()_")
char = list(string.ascii_letters + string.digits + "!@#$%^&*()_")

def generate():
         print("This is password generator. You can choose how long password you want, how many letters, digits or special characters you want to have. ")
         length = None
         letter_count = None
         spec_char_count = None
         digit_count = None
         while length is None and letter_count is None and spec_char_count is None and digit_count is None:
                  length_input = input("Enter length of your password: ")
                  letter_count_input = input ("Enter letters count: ")
                  spec_char_count_input = input("Enter special characters count: ")
                  digits_count_input = input("Enter digits count: ")

                  try:
                           length = int(length_input)
                           letter_count = int(letter_count_input)
                           spec_char_count = int(spec_char_count_input)
                           digit_count = int(digits_count_input)
                  except ValueError:
                           print("Wrong input! You must enter digit!")

         random.shuffle(char)
         char_length = letter_count + spec_char_count + digit_count
         password = [] 
         print(letter_count)
         for i in range (letter_count):
                  password.append(random.choice(letters))
         for i in range (spec_char_count):
                  password.append(random.choice(spec_char))  
         for i in range (digit_count):
                  password.append(random.choice(digits)) 
         random.shuffle(password)
         if length > char_length:
                  random.shuffle(char)
                  for i in range (length - char_length):
                           password.append(random.choice(char))
         random.shuffle(password)
         print("".join(password))

generate()
