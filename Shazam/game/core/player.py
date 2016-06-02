from choose_skill import choose_skill
#from . import choose_skill

class Player(object):

	
	def __init__(self):
		self.__exp = 0
		self.__level = 1
	
	def set_name(self, name):
		self.__name = name
	
	def set_stats(self, experience):
		self.__exp += experience
		self.__level = (self.__exp + 100)//100
		self.__health = 100 + 50 *(self.__level - 1)
		self.__mana = self.__health
	
	def set_spec(self, spec):
		self.__spec = spec
	
	def set_skills(self):
		'''use every time at the end of fight f-tion to 
		set skills power according to newly gainsed exp'''
		self.__skills = self.__spec.skillset()	
		# skills_set_per_level is a f-tion of every profession
		
	def use_skill(self):
		'''method used strictly inside fight function'''

		number_of_skills = len(self.__skills) 
		skill_keys = sorted(self.__skills)
		skill_values = [value for (key, value) in sorted(self.__skills.items())]
		
		i = 0
		while i < number_of_skills:
			print skill_keys[i], skill_values[i], "dmg"
			i += 1
		
		what_do = choose_skill(number_of_skills)
		return skill_values[what_do - 1]	#because iteration from 0
		
		

	def get_player(self):
		print "Name: ", self.__name
		print "level: ", self.__level
		print "experience: ", self.__exp
		print "health: ", self.__health
		print "mana: ", self.__mana
		
	def get_name(self):
		return self.__name

	def get_level(self):
		return self.__level
		
	def get_exp(self):
		return self.__exp
		
	def get_spec(self):
		return self.__spec
		
	def get_skills(self):
		return self.__skills
		
	def get_health(self):
		return self.__health
		
	def get_mana(self):
		return self.__mana
