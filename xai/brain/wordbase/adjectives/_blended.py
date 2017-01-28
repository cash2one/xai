

#calss header
class _BLENDED():
	def __init__(self,): 
		self.name = "BLENDED"
		self.definitions = [u'A blended drink contains two or more different types of the same product: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
