

#calss header
class _BEFOREHAND():
	def __init__(self,): 
		self.name = "BEFOREHAND"
		self.definitions = [u'earlier (than a particular time): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
