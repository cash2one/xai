

#calss header
class _INEXPRESSIBLE():
	def __init__(self,): 
		self.name = "INEXPRESSIBLE"
		self.definitions = [u'An inexpressible feeling is too strong to be described: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
