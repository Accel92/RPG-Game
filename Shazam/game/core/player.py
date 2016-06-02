from choose_skill import choose_skill

class Player(object):

	
	def __init__(self):
		self.exp = 0
		self.level = 1
	
	def set_name(self, name):
		self.name = name
	
	def set_stats(self, experience):
		self.exp += experience
		self.level = (self.exp + 100)//100
		self.health = 100 + 50 *(self.level - 1)
		self.mana = self.health
	
	def set_spec(self, spec):
		self.spec = spec
	
	def set_skills(self):
		'''use every time at the end of fight f-tion to 
		set skills power according to newly gainsed exp'''
		self.skills = self.spec.skillset()	
		# skills_set_per_level is a f-tion of every profession
		
	def use_skill(self):
		'''method used strictly inside fight function'''

		number_of_skills = len(self.skills) 
		skill_keys = sorted(self.skills)
		skill_values = [value for (key, value) in sorted(self.skills.items())]
		
		i = 0
		while i < number_of_skills:
			print skill_keys[i], skill_values[i], "dmg"
			i += 1
		
		what_do = choose_skill(number_of_skills)
		return skill_values[what_do - 1]	#because iteration from 0
		
		

	def get_player(self):
		print "Name: ", self.name
		print "level: ", self.level
		print "experience: ", self.exp
		print "health: ", self.health
		print "mana: ", self.mana
		
	def get_name(self):
		return self.name

	def get_level(self):
		return self.level
		
	def get_exp(self):
		return self.exp
		
	def get_spec(self):
		return self.spec
		
	def get_skills(self):
		return self.skills
		
	def get_health(self):
		return self.health
		
	def get_mana(self):
		return self.mana
