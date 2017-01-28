

#calss header
class _FARTHER():
	def __init__(self,): 
		self.name = "FARTHER"
		self.definitions = [u'a greater distance from something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
