

#calss header
class _PLAINLY():
	def __init__(self,): 
		self.name = "PLAINLY"
		self.definitions = [u'clearly or obviously: ', u'simply and without a lot of decoration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
