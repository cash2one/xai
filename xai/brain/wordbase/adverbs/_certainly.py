

#calss header
class _CERTAINLY():
	def __init__(self,): 
		self.name = "CERTAINLY"
		self.definitions = [u'used to reply completely or to emphasize something and show that there is no doubt about it: ', u'used when agreeing or disagreeing strongly to a request: ', u'very likely to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
