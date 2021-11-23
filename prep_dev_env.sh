#!/bin/bash
sec_secret_storage_loc="/secret_files"

echo "Script for preparing the development environment"
echo "------------------------------------------------"

echo "Checking if config.ini exists in the current working dir -->"
if test -f "config.ini"; then
    echo "exists"
else
	echo "Copying config file from secure secret storage"
	cp $HOME$sec_secret_storage_loc/config.ini .
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying config.ini file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Checking if log_generator.yaml exists in the current working dir -->"
if test -f "log_generator.yaml"; then
    echo "exists"
else
	echo "Copying log config file from local template log_generator.yaml"
	cp $HOME$sec_secret_storage_loc/log_generator.yaml .
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying log_generator.yaml file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Checking if log_migrate_db.yaml exists in the current working dir -->"
if test -f "log_migrate_db.yaml"; then
    echo "exists"
else
	echo "Copying log config file from local template log_migrate_db.yaml"
	cp $HOME$sec_secret_storage_loc/log_migrate_db.yaml .
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying log_migrate_db.yaml file"; exit 1; fi
fi
echo "------------------------------------------------"
echo "Chcecking if there is log directory -->"
if test -d "./log"; then
  echo "exists"
else
  echo "Creating new /log directory"
  mkdir log
  if [ $? -eq 0 ]; then echo "OK"; else echo "Problem making new log directory"; exit 1; fi
fi
echo "------------------------------------------------"
echo "Getting python3 executable loc"
python_exec_loc=$(which python3)
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem getting python3 exec location"; exit 1; fi
echo "$python_exec_loc"
echo "------------------------------------------------"

echo "Running config tests"
$python_exec_loc test_config.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Configuration test FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "Running DB migrations"
$python_exec_loc migrate_db.py
if [ $? -eq 0 ]; then echo "OK"; else echo "DB migration FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "Running password generator tests"
$python_exec_loc test_password_generator.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Password generator test FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "ALL SET UP! YOU ARE READY TO CODE"
echo "to start the program, execute:"
echo "$python_exec_loc password_generator.py"
