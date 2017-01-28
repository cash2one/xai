

#calss header
class _FREELY():
	def __init__(self,): 
		self.name = "FREELY"
		self.definitions = [u'without being controlled or limited: ', u'in a way that is not fixed or joined to anything, so able to move easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
