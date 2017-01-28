

#calss header
class _EVANESCENT():
	def __init__(self,): 
		self.name = "EVANESCENT"
		self.definitions = [u'lasting for only a short time, then disappearing quickly and being forgotten']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
