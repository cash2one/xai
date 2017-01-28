

#calss header
class _WHERE():
	def __init__(self,): 
		self.name = "WHERE"
		self.definitions = [u'to, at, or in what place: ', u'used when referring to a particular stage in a process or activity: ', u'in what situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
