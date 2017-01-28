

#calss header
class _DIFFIDENT():
	def __init__(self,): 
		self.name = "DIFFIDENT"
		self.definitions = [u'shy and not confident of your abilities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
