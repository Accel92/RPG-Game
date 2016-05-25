from sys import exit
import random
import time

from ..core import Fight
from ..chars1 import SpiderLv1

class AryanBunker(object):
	
	def start(self):
		print "I am Aryan."
		print "Fight!"
		spider = SpiderLv1()
		fight1 = Fight(spider, 1)
		fight1.fight()
		time.sleep(2)
		return 0
