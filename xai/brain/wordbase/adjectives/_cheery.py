

#calss header
class _CHEERY():
	def __init__(self,): 
		self.name = "CHEERY"
		self.definitions = [u'bright and happy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
