

#calss header
class _BIOCHEMICAL():
	def __init__(self,): 
		self.name = "BIOCHEMICAL"
		self.definitions = [u'connected with the chemistry of living things']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
