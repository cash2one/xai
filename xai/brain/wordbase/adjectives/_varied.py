

#calss header
class _VARIED():
	def __init__(self,): 
		self.name = "VARIED"
		self.definitions = [u'containing or changing between several different things or types: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
