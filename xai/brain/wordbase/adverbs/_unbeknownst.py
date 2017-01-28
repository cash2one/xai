

#calss header
class _UNBEKNOWNST():
	def __init__(self,): 
		self.name = "UNBEKNOWNST"
		self.definitions = [u'without a particular person knowing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
