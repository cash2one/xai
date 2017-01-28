

#calss header
class _SOUTHBOUND():
	def __init__(self,): 
		self.name = "SOUTHBOUND"
		self.definitions = [u'going or leading towards the south: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
