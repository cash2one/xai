

#calss header
class _TIGHTLY():
	def __init__(self,): 
		self.name = "TIGHTLY"
		self.definitions = [u'firmly or closely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
