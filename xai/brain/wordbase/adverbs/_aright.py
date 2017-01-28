

#calss header
class _ARIGHT():
	def __init__(self,): 
		self.name = "ARIGHT"
		self.definitions = [u'correctly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
