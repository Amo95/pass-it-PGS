import os
import time
import string
import datetime
from length import PassLength

# create db system to store and secure generated passwords
'''
from textwrap import dedent
from peewee import *

db = SqliteDatabase('reveal.db')

class ToDo(Model):
    """Model for creating to-do items. 'done' indicates that it's been completed,
    'protected' makes it immune to cleanup"""
    task = CharField(max_length=255)
    timestamp = DateTimeField(default=datetime.datetime.now)
    done = BooleanField(default=False)
    protected = BooleanField(default=False)

    class Meta:
        database = db


def initialize():
    """Connect to database, build tables if they don't exist"""
    db.connect()
    db.create_tables([ToDo], safe=True)'''

# assigning random strings for later use
strings =  dict(text = string.ascii_letters,
	numbers = string.digits,
	whitespace = string.digits,
	symbols = string.punctuation
	)
strings = "".join(list(strings.values())) # store random strings
passw = PassLength(strings) # length passed on string

def main():
	print("Select Password Length")
	choose_len = [
	"8-Length", "16-Length", 
	"24-Length", "32-Length", "Manual input"
	]

	for index, length in enumerate(choose_len, 
		start=1):
		print(f"{index}. {length}")

	select = int(input("\n>>> "))

	if select == 1:
		print(passw.eight())
	elif select == 2:
		print(passw.sixteen())
	elif select == 3:
		print(passw.twenty())
	elif select == 4:
		print(passw.thirty())
	elif select == 5:
		print("Enter length")
		lens = int(input(">> "))
		print(passw.manual(lens))
	else:
		return None

if __name__ == "__main__":
	try:
		main()
	except:
		main()