

#calss header
class _DISASTROUS():
	def __init__(self,): 
		self.name = "DISASTROUS"
		self.definitions = [u'extremely bad or unsuccessful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
