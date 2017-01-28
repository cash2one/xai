

#calss header
class _SQUARELY():
	def __init__(self,): 
		self.name = "SQUARELY"
		self.definitions = [u'directly and firmly: ', u'with weight equally balanced on each side, not to one side: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
