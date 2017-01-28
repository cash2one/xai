

#calss header
class _CORNBALL():
	def __init__(self,): 
		self.name = "CORNBALL"
		self.definitions = [u'A cornball joke, film, story, etc. has no new ideas and is not sincere, or is too often repeated and therefore not funny or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
