

#calss header
class _LOOSELY():
	def __init__(self,): 
		self.name = "LOOSELY"
		self.definitions = [u'in a way that is not firmly held or attached: ', u'not exactly: ', u'not tightly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
