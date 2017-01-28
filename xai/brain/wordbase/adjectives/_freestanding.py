

#calss header
class _FREESTANDING():
	def __init__(self,): 
		self.name = "FREESTANDING"
		self.definitions = [u'standing alone and not attached to a wall, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
