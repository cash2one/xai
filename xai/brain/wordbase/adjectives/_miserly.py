

#calss header
class _MISERLY():
	def __init__(self,): 
		self.name = "MISERLY"
		self.definitions = [u'like or typical of a miser: ', u'A miserly amount is extremely small: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
