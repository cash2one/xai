

#calss header
class _STEEPLY():
	def __init__(self,): 
		self.name = "STEEPLY"
		self.definitions = [u'suddenly or by a large amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
