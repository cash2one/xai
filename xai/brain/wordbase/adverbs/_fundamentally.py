

#calss header
class _FUNDAMENTALLY():
	def __init__(self,): 
		self.name = "FUNDAMENTALLY"
		self.definitions = [u'in a basic and important way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
