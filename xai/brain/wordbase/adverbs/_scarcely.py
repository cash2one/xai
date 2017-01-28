

#calss header
class _SCARCELY():
	def __init__(self,): 
		self.name = "SCARCELY"
		self.definitions = [u'almost not: ', u'used to say that something happened immediately after something else happened: ', u'certainly not: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
