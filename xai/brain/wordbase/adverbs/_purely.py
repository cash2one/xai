

#calss header
class _PURELY():
	def __init__(self,): 
		self.name = "PURELY"
		self.definitions = [u'only: ', u'for only one reason or purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
