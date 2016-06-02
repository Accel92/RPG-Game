from ..core import my_player
from random import randint

class SpiderLv1(object):
	
	name = "Spider"
	fight_plot = "I am bad spider sama!"
	first_hit_chance_ratio = 100
	
	def __init__(self):
		self.level = 1
		self.health = my_player.get_health() * 0.7
	
	def attack(self):
		print "Spider bites you"
		spider_dmg = randint(10, 17)
		return spider_dmg
	
	def get_health(self):
		return self.health
