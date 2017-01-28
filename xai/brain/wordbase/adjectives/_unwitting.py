

#calss header
class _UNWITTING():
	def __init__(self,): 
		self.name = "UNWITTING"
		self.definitions = [u'without knowing or planning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
