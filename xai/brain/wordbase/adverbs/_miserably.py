

#calss header
class _MISERABLY():
	def __init__(self,): 
		self.name = "MISERABLY"
		self.definitions = [u'feeling or showing unhappiness: ', u'in a way that is very unpleasant and makes you unhappy: ', u'having little value, in a way that is disappointing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
