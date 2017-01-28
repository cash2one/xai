

#calss header
class _NETHER():
	def __init__(self,): 
		self.name = "NETHER"
		self.definitions = [u'in a lower position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
