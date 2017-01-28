

#calss header
class _IDENTICAL():
	def __init__(self,): 
		self.name = "IDENTICAL"
		self.definitions = [u'exactly the same, or very similar: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
