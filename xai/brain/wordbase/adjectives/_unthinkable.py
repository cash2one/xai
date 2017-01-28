

#calss header
class _UNTHINKABLE():
	def __init__(self,): 
		self.name = "UNTHINKABLE"
		self.definitions = [u'so shocking that it cannot be imagined as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
