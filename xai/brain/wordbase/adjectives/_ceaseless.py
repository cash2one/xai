

#calss header
class _CEASELESS():
	def __init__(self,): 
		self.name = "CEASELESS"
		self.definitions = [u'without stopping, or seeming to have no end']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
