

#calss header
class _ANON():
	def __init__(self,): 
		self.name = "ANON"
		self.definitions = [u'soon or in the near future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
