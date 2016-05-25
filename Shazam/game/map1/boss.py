from sys import exit
import random
import time

class Boss(object):

	def start(self):
		print "I am Boss, fight me!"
		time.sleep(0.5)
		print "What do you do?"
		print "1. Fight."
		what_do = raw_input("> ")
		if what_do == "1":
			print "You won, hurray!"
			a = raw_input("Press any key to exit:\n>")
			exit(0)
			
		else:
			print "You can't do it, again."
			foo = Boss()
			foo.start()
