

#calss header
class _INEXPERT():
	def __init__(self,): 
		self.name = "INEXPERT"
		self.definitions = [u'having little skill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
