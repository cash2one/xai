

#calss header
class _PALATIAL():
	def __init__(self,): 
		self.name = "PALATIAL"
		self.definitions = [u'A palatial house is very large and beautiful.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
