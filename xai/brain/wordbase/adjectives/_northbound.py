

#calss header
class _NORTHBOUND():
	def __init__(self,): 
		self.name = "NORTHBOUND"
		self.definitions = [u'going or leading towards the north: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
