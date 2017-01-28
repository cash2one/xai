

#calss header
class _FRANKLY():
	def __init__(self,): 
		self.name = "FRANKLY"
		self.definitions = [u'in an honest and direct way: ', u'used when giving an honest and direct opinion, often one that might upset someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
