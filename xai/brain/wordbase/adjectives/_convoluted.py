

#calss header
class _CONVOLUTED():
	def __init__(self,): 
		self.name = "CONVOLUTED"
		self.definitions = [u'very twisted: ', u'Convoluted sentences, explanations, arguments, etc. are unreasonably long and difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
