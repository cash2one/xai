

#calss header
class _DUMPY():
	def __init__(self,): 
		self.name = "DUMPY"
		self.definitions = [u'short and fat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
