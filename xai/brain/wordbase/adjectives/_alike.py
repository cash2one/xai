

#calss header
class _ALIKE():
	def __init__(self,): 
		self.name = "ALIKE"
		self.definitions = [u'similar to each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
