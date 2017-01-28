

#calss header
class _SPINDLY():
	def __init__(self,): 
		self.name = "SPINDLY"
		self.definitions = [u'long or tall and thin, and looking weak: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
