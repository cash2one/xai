

#calss header
class _AXIOMATIC():
	def __init__(self,): 
		self.name = "AXIOMATIC"
		self.definitions = [u'obviously true and therefore not needing to be proved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
