

#calss header
class _IDEALLY():
	def __init__(self,): 
		self.name = "IDEALLY"
		self.definitions = [u'used when describing the perfect situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
