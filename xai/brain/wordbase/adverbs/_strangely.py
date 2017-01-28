

#calss header
class _STRANGELY():
	def __init__(self,): 
		self.name = "STRANGELY"
		self.definitions = [u'in a way that is unusual, unexpected, or difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
