

#calss header
class _REASONABLY():
	def __init__(self,): 
		self.name = "REASONABLY"
		self.definitions = [u'using good judgment: ', u'in a satisfactory way: ', u'at a price that is not too expensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
