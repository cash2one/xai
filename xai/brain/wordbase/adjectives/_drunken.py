

#calss header
class _DRUNKEN():
	def __init__(self,): 
		self.name = "DRUNKEN"
		self.definitions = [u'A drunken person is (often) under the influence of alcohol: ', u'used to describe a situation in which a lot of alcohol has been drunk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
