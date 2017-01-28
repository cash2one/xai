

#calss header
class _WORST():
	def __init__(self,): 
		self.name = "WORST"
		self.definitions = [u'the most badly: ', u'used to emphasize what is worst about a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
