

#calss header
class _SECOND():
	def __init__(self,): 
		self.name = "SECOND"
		self.definitions = [u'after the first and before any others: ', u'used to introduce the second thing in a list of things you want to say or write: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
