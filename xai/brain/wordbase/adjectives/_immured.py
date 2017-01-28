

#calss header
class _IMMURED():
	def __init__(self,): 
		self.name = "IMMURED"
		self.definitions = [u'kept as a prisoner or closed away and out of sight: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
