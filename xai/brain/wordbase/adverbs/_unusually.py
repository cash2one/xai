

#calss header
class _UNUSUALLY():
	def __init__(self,): 
		self.name = "UNUSUALLY"
		self.definitions = [u'more than is usual or expected, or in a way that is not usual: ', u'in a way that is not usual for someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
