

#calss header
class _PRECIPITATELY():
	def __init__(self,): 
		self.name = "PRECIPITATELY"
		self.definitions = [u'in a way that is too sudden and done without thinking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
