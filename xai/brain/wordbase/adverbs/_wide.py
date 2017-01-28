

#calss header
class _WIDE():
	def __init__(self,): 
		self.name = "WIDE"
		self.definitions = [u'farther than usual, or as far as possible: ', u'completely, or by a large amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
