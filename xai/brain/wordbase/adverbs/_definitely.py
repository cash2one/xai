

#calss header
class _DEFINITELY():
	def __init__(self,): 
		self.name = "DEFINITELY"
		self.definitions = [u'without any doubt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
