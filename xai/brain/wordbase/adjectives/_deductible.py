

#calss header
class _DEDUCTIBLE():
	def __init__(self,): 
		self.name = "DEDUCTIBLE"
		self.definitions = [u'A deductible amount can be taken away from a total: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
