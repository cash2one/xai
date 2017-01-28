

#calss header
class _URBAN():
	def __init__(self,): 
		self.name = "URBAN"
		self.definitions = [u'of or in a city or town: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
