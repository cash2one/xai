

#calss header
class _STOUTLY():
	def __init__(self,): 
		self.name = "STOUTLY"
		self.definitions = [u'in a firm and determined way: ', u'in a strong way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
