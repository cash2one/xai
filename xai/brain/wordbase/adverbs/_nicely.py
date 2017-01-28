

#calss header
class _NICELY():
	def __init__(self,): 
		self.name = "NICELY"
		self.definitions = [u'well, pleasantly, or in a satisfactory way: ', u'in a kind, friendly, or polite way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
