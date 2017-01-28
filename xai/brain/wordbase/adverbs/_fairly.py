

#calss header
class _FAIRLY():
	def __init__(self,): 
		self.name = "FAIRLY"
		self.definitions = [u'more than average, but less than very: ', u'used to emphasize figurative expressions that describe what people or objects are doing: ', u'If you do something fairly, you do it in a way that is right and reasonable and treats people equally: ', u'completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
