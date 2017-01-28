

#calss header
class _CONCRETELY():
	def __init__(self,): 
		self.name = "CONCRETELY"
		self.definitions = [u'in a clear and definite way, or in a form that can be seen or felt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
