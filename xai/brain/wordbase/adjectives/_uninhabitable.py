

#calss header
class _UNINHABITABLE():
	def __init__(self,): 
		self.name = "UNINHABITABLE"
		self.definitions = [u'not habitable (= suitable to live in): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
