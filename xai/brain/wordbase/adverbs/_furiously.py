

#calss header
class _FURIOUSLY():
	def __init__(self,): 
		self.name = "FURIOUSLY"
		self.definitions = [u'in a very angry way: ', u'with as much effort or strength as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
