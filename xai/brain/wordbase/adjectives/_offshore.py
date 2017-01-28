

#calss header
class _OFFSHORE():
	def __init__(self,): 
		self.name = "OFFSHORE"
		self.definitions = [u'away from or at a distance from the coast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
