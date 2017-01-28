

#calss header
class _SURPRISING():
	def __init__(self,): 
		self.name = "SURPRISING"
		self.definitions = [u'unexpected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
