

#calss header
class _MECHANICALLY():
	def __init__(self,): 
		self.name = "MECHANICALLY"
		self.definitions = [u'using or relating to machines: ', u'without thinking about what you are doing, especially because you do something often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
