

#calss header
class _HARDLY():
	def __init__(self,): 
		self.name = "HARDLY"
		self.definitions = [u'only just; almost not: ', u'certainly not: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
