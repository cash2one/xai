

#calss header
class _NECESSARILY():
	def __init__(self,): 
		self.name = "NECESSARILY"
		self.definitions = [u'used in negatives to mean "in every case" or "therefore": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
