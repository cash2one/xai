

#calss header
class _PERCENT():
	def __init__(self,): 
		self.name = "PERCENT"
		self.definitions = [u'for or out of every 100, shown by the symbol %: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
