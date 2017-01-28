

#calss header
class _DIAMETRICALLY():
	def __init__(self,): 
		self.name = "DIAMETRICALLY"
		self.definitions = [u'completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
