

#calss header
class _DRAMATICALLY():
	def __init__(self,): 
		self.name = "DRAMATICALLY"
		self.definitions = [u'suddenly or obviously: ', u'(as if) acting in a play: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
