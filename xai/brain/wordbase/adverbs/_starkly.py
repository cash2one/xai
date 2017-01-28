

#calss header
class _STARKLY():
	def __init__(self,): 
		self.name = "STARKLY"
		self.definitions = [u'very obviously and clearly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
