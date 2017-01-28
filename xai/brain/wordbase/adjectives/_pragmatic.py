

#calss header
class _PRAGMATIC():
	def __init__(self,): 
		self.name = "PRAGMATIC"
		self.definitions = [u'solving problems in a sensible way that suits the conditions that really exist now, rather than obeying fixed theories, ideas, or rules: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
