from password_generator import *

print("Password generator test")
print("-----------")
print("Testing function /mysql_check_if_password_exists_in_db")
assert mysql_check_if_password_exists_in_db("parolestests") == 0

print("OK")
print("-----------")
