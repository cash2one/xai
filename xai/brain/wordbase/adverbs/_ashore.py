

#calss header
class _ASHORE():
	def __init__(self,): 
		self.name = "ASHORE"
		self.definitions = [u'towards or onto land from an area of water: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
