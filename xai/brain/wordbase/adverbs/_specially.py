

#calss header
class _SPECIALLY():
	def __init__(self,): 
		self.name = "SPECIALLY"
		self.definitions = [u'extremely or in particular: ', u'for a particular purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
