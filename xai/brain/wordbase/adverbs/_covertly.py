

#calss header
class _COVERTLY():
	def __init__(self,): 
		self.name = "COVERTLY"
		self.definitions = [u'secretly, or in a hidden way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
