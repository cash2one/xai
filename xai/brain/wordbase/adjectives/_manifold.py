

#calss header
class _MANIFOLD():
	def __init__(self,): 
		self.name = "MANIFOLD"
		self.definitions = [u'many and of several different types: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
