

#calss header
class _INDEFINITELY():
	def __init__(self,): 
		self.name = "INDEFINITELY"
		self.definitions = [u'for a period of time with no fixed end: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
