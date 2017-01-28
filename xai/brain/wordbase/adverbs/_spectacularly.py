

#calss header
class _SPECTACULARLY():
	def __init__(self,): 
		self.name = "SPECTACULARLY"
		self.definitions = [u'in a very beautiful way that people admire: ', u'extremely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
