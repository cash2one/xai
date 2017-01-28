

#calss header
class _JURASSIC():
	def __init__(self,): 
		self.name = "JURASSIC"
		self.definitions = [u'from or referring to the period of time between around 208 and 146 million years ago, in which the first birds appeared and the single piece of land broke up into separate continents: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
