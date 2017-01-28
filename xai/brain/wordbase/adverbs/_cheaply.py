

#calss header
class _CHEAPLY():
	def __init__(self,): 
		self.name = "CHEAPLY"
		self.definitions = [u'for a low cost or price: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
