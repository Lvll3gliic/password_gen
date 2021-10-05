import logging
import logging.config
import mysql.connector
import requests
import json
import yaml
import string
import random

from configparser import ConfigParser
from mysql.connector import Error

# defineju mainigos no kuriem tiks veidotas paroles
letters = list(string.ascii_letters)
digits = list(string.digits)
spec_char = list("!@#$%^&*()_")
char = list(string.ascii_letters + string.digits + "!@#$%^&*()_")

with open('./log_generator.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)

logger = logging.getLogger('root')
logger.info('Password generator')
logger.info('Loading configuration from file')

try:
	config = ConfigParser()
	config.read('config.ini')

	mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
	mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
	mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
	mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')

except:
	logger.exception('')
logger.info('DONE')

connection = None
connected = False

def init_db():
	global connection
	connection = mysql.connector.connect(host=mysql_config_mysql_host, database = mysql_config_mysql_db, user = mysql_config_mysql_user, password = mysql_config_mysql_pass)

init_db()

def get_cursor():
	global connection
	try:
		connection.ping(reconnect=True, attempts=1, delay=0)
		connection.commit()
	except mysql.connector.Error as err:
		logger.error("No connection to db " + str(err))
		connection = init_db()
		connection.commit()
	return connection.cursor()
logger.info('Connecting to MySQL DB')
try:
	# connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
	cursor = get_cursor()
	if connection.is_connected():
		db_Info = connection.get_server_info()
		logger.info('Connected to MySQL database. MySQL Server version on ' + str(db_Info))
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		logger.debug('Your connected to - ' + str(record))
		connection.commit()
except Error as e :
	logger.error('Error while connecting to MySQL' + str(e))

# Check if table exists
def mysql_check_if_password_exists_in_db(password):
    records = []
    cursor = get_cursor()
    try:
        cursor = connection.cursor()
        result = cursor.execute("SELECT password FROM used_passwords WHERE password = 'str(password)'")
        records = cursor.fetchall()
        connection.commit()
    except Error as e:
        logger.error("SELECT password FROM used_passwords WHERE password = 'str(pass)'")
        logger.error('Problem checking if that password exists: ' + str(e))
        pass
    return len(records)

def mysql_insert_password_into_db(password, letters, digits, spec_char, length):
    cursor = get_cursor()
    try:
        cursor = connection.cursor()
        #result = cursor.execute("INSERT INTO used_passwords(password, letters, digits, spec_char, lenght) VALUES ('str(password)', int(letters), 'int(digits)', 'int(spec_char)', 'int(length)')")
        #result = cursor.execute("INSERT INTO used_passwords(password, letters, digits, spec_char, lenght) VALUES (?,?,?,?,?)", (str(password), int(letters), int(digits), int(spec_char), int(length)))
        add_password =("INSERT INTO used_passwords(password, letters, digits, spec_char, lenght) VALUES (%s, %s, %s, %s, %s)")
        data = (str(password), int(letters), int(digits), int(spec_char), int(length))
        cursor.execute(add_password, data)
        connection.commit()
    except Error as e:
        logger.error("INSERT INTO used_passwords(password, letters, digits, spec_char, lenght) VALUES ('str(password)', 'int(letters)', 'int(digits)', 'int(spec_char)', 'int(length)')")
        logger.error('Problem inserting password into db: ' + str(e))
        pass

def push_password_to_db(password, letters, digits, spec_char, length):
    if mysql_check_if_password_exists_in_db(password) == 0:
        logger.debug('Password is not in DB')
        mysql_insert_password_into_db(password, letters, digits, spec_char, length)
    else:
        logger.debug('Password is already in our DB')

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
         push_password_to_db(password, letter_count, digit_count, spec_char_count, length)
         #tiek konsole izprinteta parole
         print( 'Your unique password: ', "".join(password))

generate()
