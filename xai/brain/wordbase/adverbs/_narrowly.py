

#calss header
class _NARROWLY():
	def __init__(self,): 
		self.name = "NARROWLY"
		self.definitions = [u'only by a small amount: ', u'in a limited way: ', u'carefully or in a way that shows doubt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
