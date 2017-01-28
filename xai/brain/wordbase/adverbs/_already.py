

#calss header
class _ALREADY():
	def __init__(self,): 
		self.name = "ALREADY"
		self.definitions = [u'before the present time: ', u'earlier than the time expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
