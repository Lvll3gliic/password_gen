import string
import random
# defineju mainigos no kuriem tiks veidotas paroles
letters = list(string.ascii_letters)
digits = list(string.digits)
spec_char = list("!@#$%^&*()_")
char = list(string.ascii_letters + string.digits + "!@#$%^&*()_")
# defineju funkciju, kas pieprasis lietotaja datu ievadi un pectam izveidos paroli
def generate():
         print("This is password generator. You can choose how long password you want, how many letters, digits or special characters you want to have. ")
         length = None
         letter_count = None
         spec_char_count = None
         digit_count = None
         # tiek definets cikls, kamer visi no siem parametriem ir None, tas izprintes, ka ir problema un saks no jauna, kamer tiks ievaditi pareizi dati
         while length is None and letter_count is None and spec_char_count is None and digit_count is None:
                  # lietotaja datu ievade
                  length_input = input("Enter length of your password: ")
                  letter_count_input = input ("Enter letters count: ")
                  spec_char_count_input = input("Enter special characters count: ")
                  digits_count_input = input("Enter digits count: ")
                  # megina parset datus uz int, ja nesanak, izprinte, ka neizdevas un sak no jauna ciklu
                  try:
                           length = int(length_input)
                           letter_count = int(letter_count_input)
                           spec_char_count = int(spec_char_count_input)
                           digit_count = int(digits_count_input)
                  except ValueError:
                           print("Wrong input! You must enter digit!")
         # randominize char lista simbolus
         random.shuffle(char)
         #saskaitu lietotaja ievaditos datus, lai saprastu, cik gara parole sanak
         char_length = letter_count + spec_char_count + digit_count
         # ja lietotaja ievadito simbolu skaits parsniedz paroles garumu, izprinte kludu un sak no jauna
         if char_length > length:
                  print("You have done it wrong, try again!")
                  return generate()
         password = []
         # cikls, kas izvelas lietotaja noradito simbolu skaitu, lai no lista panemtu simbolus
         for i in range (letter_count):
                  password.append(random.choice(letters))
         for i in range (spec_char_count):
                  password.append(random.choice(spec_char))
         for i in range (digit_count):
                  password.append(random.choice(digits))

         random.shuffle(password)
         # ja noraditais paroles garums ir lielaks par izveleto simbolu skaitu, tad pievieno atlikusos simbolus random
         if length > char_length:
                  random.shuffle(char)
                  for i in range (length - char_length):
                           password.append(random.choice(char))
         random.shuffle(password)
         #tiek konsole izprinteta parole
         print("".join(password))

generate()
