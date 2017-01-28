

#calss header
class _BASELESS():
	def __init__(self,): 
		self.name = "BASELESS"
		self.definitions = [u'not based on facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
