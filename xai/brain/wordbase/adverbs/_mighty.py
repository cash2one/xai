

#calss header
class _MIGHTY():
	def __init__(self,): 
		self.name = "MIGHTY"
		self.definitions = [u'very: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
