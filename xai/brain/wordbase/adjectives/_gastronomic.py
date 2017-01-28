

#calss header
class _GASTRONOMIC():
	def __init__(self,): 
		self.name = "GASTRONOMIC"
		self.definitions = [u'relating to the preparation and consumption (= eating) of good food: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
