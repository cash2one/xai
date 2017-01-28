

#calss header
class _HANDILY():
	def __init__(self,): 
		self.name = "HANDILY"
		self.definitions = [u'in a useful or convenient way: ', u'easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
