

#calss header
class _FECKLESS():
	def __init__(self,): 
		self.name = "FECKLESS"
		self.definitions = [u'weak in character and lacking determination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
