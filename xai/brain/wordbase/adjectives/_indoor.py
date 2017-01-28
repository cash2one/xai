

#calss header
class _INDOOR():
	def __init__(self,): 
		self.name = "INDOOR"
		self.definitions = [u'happening, used, or existing inside a building: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
