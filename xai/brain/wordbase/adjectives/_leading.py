

#calss header
class _LEADING():
	def __init__(self,): 
		self.name = "LEADING"
		self.definitions = [u'very important or most important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
