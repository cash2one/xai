

#calss header
class _ALL():
	def __init__(self,): 
		self.name = "ALL"
		self.definitions = [u'completely: ', u'used after a number to mean that both teams or players in a game have equal points: ', u'almost: ', u'in every way: ', u'even or much better, stronger, more exciting, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
