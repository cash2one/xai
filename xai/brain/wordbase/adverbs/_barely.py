

#calss header
class _BARELY():
	def __init__(self,): 
		self.name = "BARELY"
		self.definitions = [u'by the smallest amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
