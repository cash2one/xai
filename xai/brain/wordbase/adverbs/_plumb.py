

#calss header
class _PLUMB():
	def __init__(self,): 
		self.name = "PLUMB"
		self.definitions = [u'exactly: ', u'completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
