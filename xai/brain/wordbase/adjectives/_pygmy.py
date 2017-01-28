

#calss header
class _PYGMY():
	def __init__(self,): 
		self.name = "PYGMY"
		self.definitions = [u'A pygmy animal or bird is one of a type that is smaller than animals or birds of that type usually are: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
