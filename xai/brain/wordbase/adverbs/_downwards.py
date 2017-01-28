

#calss header
class _DOWNWARDS():
	def __init__(self,): 
		self.name = "DOWNWARDS"
		self.definitions = [u'towards a lower position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
