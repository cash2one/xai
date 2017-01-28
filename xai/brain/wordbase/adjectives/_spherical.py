

#calss header
class _SPHERICAL():
	def __init__(self,): 
		self.name = "SPHERICAL"
		self.definitions = [u'round, like a ball: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
