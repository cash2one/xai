

#calss header
class _DRAUGHTY():
	def __init__(self,): 
		self.name = "DRAUGHTY"
		self.definitions = [u'A draughty place, especially a room, has currents of unpleasantly cold air blowing through it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
