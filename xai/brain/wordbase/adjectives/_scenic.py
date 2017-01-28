

#calss header
class _SCENIC():
	def __init__(self,): 
		self.name = "SCENIC"
		self.definitions = [u'having or allowing you to see beautiful natural features: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
