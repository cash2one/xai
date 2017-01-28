

#calss header
class _DISADVANTAGED():
	def __init__(self,): 
		self.name = "DISADVANTAGED"
		self.definitions = [u'not having the standard of living conditions, education, etc. that most people have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
