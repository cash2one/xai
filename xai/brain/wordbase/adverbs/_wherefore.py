

#calss header
class _WHEREFORE():
	def __init__(self,): 
		self.name = "WHEREFORE"
		self.definitions = [u'for what reason; why: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
