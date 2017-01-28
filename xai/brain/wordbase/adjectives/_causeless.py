

#calss header
class _CAUSELESS():
	def __init__(self,): 
		self.name = "CAUSELESS"
		self.definitions = [u'without any good reason: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
