

#calss header
class _TOLLED():
	def __init__(self,): 
		self.name = "TOLLED"
		self.definitions = [u'A tolled road, bridge, etc. is one that you pay to use: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
