

#calss header
class _CHICKEN():
	def __init__(self,): 
		self.name = "CHICKEN"
		self.definitions = [u'not brave: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
