

#calss header
class _PURPORTEDLY():
	def __init__(self,): 
		self.name = "PURPORTEDLY"
		self.definitions = [u'in a way that is stated to be true, although this may not be the case: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
