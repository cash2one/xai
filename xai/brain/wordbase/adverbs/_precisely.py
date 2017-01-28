

#calss header
class _PRECISELY():
	def __init__(self,): 
		self.name = "PRECISELY"
		self.definitions = [u'exactly: ', u'used to emphasize what you are saying: ', u'used to express complete agreement with someone or suggest that what they have said is obvious: ', u'carefully and accurately: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
