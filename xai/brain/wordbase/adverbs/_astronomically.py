

#calss header
class _ASTRONOMICALLY():
	def __init__(self,): 
		self.name = "ASTRONOMICALLY"
		self.definitions = [u'in a way that is connected with astronomy: ', u'by a very large amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
