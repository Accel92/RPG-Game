class Engine(object):
	
	def __init__(self, a_map):
		self.map = a_map
		
	def play(self):
		current_scene = self.map.get_first_location()
		last_scene = self.map.get_last_location()
		
		while True:
			try: 
				next_scene_return = current_scene.start()
			except AttributeError:
				last_scene.start()
				break
			current_scene = self.map.next_location(next_scene_return)
