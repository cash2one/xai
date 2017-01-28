

#calss header
class _EMPIRICAL():
	def __init__(self,): 
		self.name = "EMPIRICAL"
		self.definitions = [u'based on what is experienced or seen rather than on theory: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
