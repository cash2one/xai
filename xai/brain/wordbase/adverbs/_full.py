

#calss header
class _FULL():
	def __init__(self,): 
		self.name = "FULL"
		self.definitions = [u'to understand a situation completely: ', u'straight; directly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
