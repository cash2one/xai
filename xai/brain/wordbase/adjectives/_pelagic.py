

#calss header
class _PELAGIC():
	def __init__(self,): 
		self.name = "PELAGIC"
		self.definitions = [u'relating to or living in areas of the sea away from the land: ', u'(of fish) living near the surface of the sea: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
