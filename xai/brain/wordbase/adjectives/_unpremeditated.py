

#calss header
class _UNPREMEDITATED():
	def __init__(self,): 
		self.name = "UNPREMEDITATED"
		self.definitions = [u'(especially of a crime or something unpleasant) done without being planned']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
