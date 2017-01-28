

#calss header
class _CAUSAL():
	def __init__(self,): 
		self.name = "CAUSAL"
		self.definitions = [u'a relationship, link, etc. between two things in which one causes the other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
