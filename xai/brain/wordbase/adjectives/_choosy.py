

#calss header
class _CHOOSY():
	def __init__(self,): 
		self.name = "CHOOSY"
		self.definitions = [u'difficult to please because you are very exact about what you like: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
