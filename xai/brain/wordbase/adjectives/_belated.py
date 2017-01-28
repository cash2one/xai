

#calss header
class _BELATED():
	def __init__(self,): 
		self.name = "BELATED"
		self.definitions = [u'coming later than expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
