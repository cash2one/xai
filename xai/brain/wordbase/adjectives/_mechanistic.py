

#calss header
class _MECHANISTIC():
	def __init__(self,): 
		self.name = "MECHANISTIC"
		self.definitions = [u'thinking of living things as if they were machines: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
