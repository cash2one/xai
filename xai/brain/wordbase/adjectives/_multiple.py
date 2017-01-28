

#calss header
class _MULTIPLE():
	def __init__(self,): 
		self.name = "MULTIPLE"
		self.definitions = [u'very many of the same type, or of different types: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
