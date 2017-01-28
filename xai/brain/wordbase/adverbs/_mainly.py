

#calss header
class _MAINLY():
	def __init__(self,): 
		self.name = "MAINLY"
		self.definitions = [u'usually or to a large degree: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
