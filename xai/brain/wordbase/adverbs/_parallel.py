

#calss header
class _PARALLEL():
	def __init__(self,): 
		self.name = "PARALLEL"
		self.definitions = [u'in a position that is always the same distance from something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
