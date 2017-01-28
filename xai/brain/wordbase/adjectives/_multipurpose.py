

#calss header
class _MULTIPURPOSE():
	def __init__(self,): 
		self.name = "MULTIPURPOSE"
		self.definitions = [u'A multipurpose tool, etc. can be used in several different ways: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
