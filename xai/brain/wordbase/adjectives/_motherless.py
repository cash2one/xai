

#calss header
class _MOTHERLESS():
	def __init__(self,): 
		self.name = "MOTHERLESS"
		self.definitions = [u'without a mother: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
