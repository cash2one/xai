

#calss header
class _MANIFESTLY():
	def __init__(self,): 
		self.name = "MANIFESTLY"
		self.definitions = [u'very obviously: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
