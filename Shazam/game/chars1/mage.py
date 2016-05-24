from ..core import my_player

class Mage(object):

	def skillset(self):
		
		player_level = my_player.get_level()
		player_hp = my_player.get_health()
		
		if player_level < 3:
			skills_dict = {
			"1. Fireball: " : player_hp * 1/6,
			"2. Scorched Earth: " : player_hp * 1/5
			}	
			return skills_dict
			
		elif player_level >= 6:
			skills_dict = {
			"1. Fireball: " : player_hp * 1/6,
			"2. Scorched Earth: " : player_hp * 1/5,
			"3. Nuke: " : player_hp
			}
			return skills_dict
