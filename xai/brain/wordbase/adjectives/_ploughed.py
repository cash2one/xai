

#calss header
class _PLOUGHED():
	def __init__(self,): 
		self.name = "PLOUGHED"
		self.definitions = [u'dug to make ready for planting seeds: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
