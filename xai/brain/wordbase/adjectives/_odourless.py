

#calss header
class _ODOURLESS():
	def __init__(self,): 
		self.name = "ODOURLESS"
		self.definitions = [u'without a smell: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
