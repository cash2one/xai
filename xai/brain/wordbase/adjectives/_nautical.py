

#calss header
class _NAUTICAL():
	def __init__(self,): 
		self.name = "NAUTICAL"
		self.definitions = [u'relating to ships, sailing, or sailors: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
