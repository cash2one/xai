

#calss header
class _ARCHITECTURAL():
	def __init__(self,): 
		self.name = "ARCHITECTURAL"
		self.definitions = [u'relating to architecture: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
