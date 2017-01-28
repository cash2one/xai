

#calss header
class _INACCESSIBLE():
	def __init__(self,): 
		self.name = "INACCESSIBLE"
		self.definitions = [u'very difficult or impossible to travel to: ', u'difficult to understand or admire: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
