

#calss header
class _IRRITABLE():
	def __init__(self,): 
		self.name = "IRRITABLE"
		self.definitions = [u'becoming annoyed very easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
