

#calss header
class _FOGBOUND():
	def __init__(self,): 
		self.name = "FOGBOUND"
		self.definitions = [u'prevented from operating as usual or travelling because of fog: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
