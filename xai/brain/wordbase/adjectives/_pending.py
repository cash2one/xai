

#calss header
class _PENDING():
	def __init__(self,): 
		self.name = "PENDING"
		self.definitions = [u'about to happen or waiting to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
