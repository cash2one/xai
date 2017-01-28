

#calss header
class _OBSTREPEROUS():
	def __init__(self,): 
		self.name = "OBSTREPEROUS"
		self.definitions = [u'difficult to deal with and noisy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
