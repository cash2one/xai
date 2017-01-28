

#calss header
class _SEQUENTIAL():
	def __init__(self,): 
		self.name = "SEQUENTIAL"
		self.definitions = [u'following a particular order: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
