

#calss header
class _USUALLY():
	def __init__(self,): 
		self.name = "USUALLY"
		self.definitions = [u'in the way that most often happens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
