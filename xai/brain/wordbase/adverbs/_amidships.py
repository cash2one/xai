

#calss header
class _AMIDSHIPS():
	def __init__(self,): 
		self.name = "AMIDSHIPS"
		self.definitions = [u'in the middle part of a ship']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
