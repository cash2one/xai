

#calss header
class _FULLY():
	def __init__(self,): 
		self.name = "FULLY"
		self.definitions = [u'completely: ', u'as much as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
