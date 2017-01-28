

#calss header
class _UNBELIEVABLY():
	def __init__(self,): 
		self.name = "UNBELIEVABLY"
		self.definitions = [u'in a way that is very surprising or difficult to believe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
