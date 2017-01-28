

#calss header
class _COEDUCATIONAL():
	def __init__(self,): 
		self.name = "COEDUCATIONAL"
		self.definitions = [u'having male and female students being taught together in the same school or college rather than separately: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
