

#calss header
class _FLUTED():
	def __init__(self,): 
		self.name = "FLUTED"
		self.definitions = [u'If an object, especially a round object, is fluted, its edges have many curves that go in and out: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
