from sys import exit
import random
import time

class Fight(object):
	

	def __init__(self, type_of_mob, mob_lvl):
		self.mob = type_of_mob
		self.mob_lvl = mob_lvl
		
	def fight(self):
		
		from . import my_player
		
		player_name = my_player.get_name()
		player_hp = my_player.get_health()
		
		mob_name = self.mob.name
		mob_hp = self.mob.get_health()
		
		print self.mob.fight_plot   # fight_plot is defined with mob_lvl in it
		
		mob_hit_chance = random.randint(0,100)
		if self.mob.first_hit_chance_ratio >= mob_hit_chance:
			
			mob_dmg = self.mob.attack()
			player_hp -= mob_dmg
			print ""
			print "%s's attacked you for %s dmg" %(mob_name, mob_dmg)
			time.sleep(1)
			if player_hp < 0:
				print "You lose"
				exit(0)
		print "%s's hp is %s" %(mob_name, mob_hp)
		
		while player_hp > 0 and mob_hp > 0:
			
			time.sleep(1)
			player_dmg = my_player.use_skill()
			mob_hp -= player_dmg
			print ""
			print "Player %s attacked mob for %s dmg" %(player_name, player_dmg)
			time.sleep(1)
			if mob_hp < 0:	
				print "%s's hp is %s now" %(mob_name, mob_hp)
				break
			
			mob_dmg = self.mob.attack()
			player_hp -= mob_dmg
			print "%s attacked you for %s dmg" %(mob_name, mob_dmg)
			time.sleep(1)
			print ""
			print "%s's hp is %s now" %(mob_name, mob_hp)
			print "%s's hp is %s now" % (player_name, player_hp)	
			time.sleep(1.5)
		
		if player_hp > 0:
			print "You win"
		else: 
			print "You lose"
			
		my_player.set_stats
		my_player.set_skills
