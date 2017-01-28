

#calss header
class _RESPECTABLY():
	def __init__(self,): 
		self.name = "RESPECTABLY"
		self.definitions = [u'in a respectable way: ', u'in a way that achieves a reasonable result: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
