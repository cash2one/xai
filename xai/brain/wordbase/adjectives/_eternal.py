

#calss header
class _ETERNAL():
	def __init__(self,): 
		self.name = "ETERNAL"
		self.definitions = [u'lasting forever or for a very long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
