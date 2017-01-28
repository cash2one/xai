

#calss header
class _INDEED():
	def __init__(self,): 
		self.name = "INDEED"
		self.definitions = [u'really or certainly, often used to emphasize something: ', u'used to express that something is correct: ', u'used to add some extra information that develops or supports something you have just said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
