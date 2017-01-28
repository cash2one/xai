

#calss header
class _MASSIVE():
	def __init__(self,): 
		self.name = "MASSIVE"
		self.definitions = [u'very large in size, amount, or number: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
