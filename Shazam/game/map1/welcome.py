from sys import exit
import random
import time

from ..chars1 import Knight
from ..chars1 import Mage

from ..core import my_player

class Welcome(object):
	
	def start(self):
		
		print "Hi there, this is a game, first class (Welcome)"
		print "is being run now, have fun."
		
		print "Who are you?, What is your name?"
		name = raw_input("\n>")
		setattr(my_player, "name", name)
		print "Your name is: %s" % my_player.get_name()
		
		print "What is your speciality?"
		print "\n1. I'm knight, I cut my opponents through"
		print "2. I'm mage, I spellcast magic to wipe out my enemies"
		num_spec = raw_input(">")
		if num_spec == "1":
			spec = Knight()	
		elif num_spec == "2":
			spec = Mage()
		else:
			print "Wrong choice\n"
			Welcome.start()
		
		my_player.set_spec(spec)
		my_player.set_skills()
		print "We will proceed when we reach zero:\n"
		i = 1
		while i > 0:
			print i
			i -= 1
			time.sleep(1)
		return 'aryan'
