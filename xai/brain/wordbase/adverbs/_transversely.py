

#calss header
class _TRANSVERSELY():
	def __init__(self,): 
		self.name = "TRANSVERSELY"
		self.definitions = [u'going from side to side: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
