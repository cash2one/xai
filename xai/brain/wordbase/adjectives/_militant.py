

#calss header
class _MILITANT():
	def __init__(self,): 
		self.name = "MILITANT"
		self.definitions = [u'active, determined, and often willing to use force: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
