

#calss header
class _GENERICALLY():
	def __init__(self,): 
		self.name = "GENERICALLY"
		self.definitions = [u'relating to generic products, especially medical drugs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
