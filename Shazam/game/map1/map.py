from . import Welcome
from . import AryanBunker
from . import Boss


class Map:
	
	first_location = Welcome()
	last_location = Boss()
	
	locations = { 
	'aryan' : AryanBunker(),
	}
	
	def get_first_location(self):
		return self.first_location
	
	def get_last_location(self):
		return self.last_location
	
	def next_location(self, location):
		loc = Map.locations.get(location)
		return loc
