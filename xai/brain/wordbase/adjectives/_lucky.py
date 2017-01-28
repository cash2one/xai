

#calss header
class _LUCKY():
	def __init__(self,): 
		self.name = "LUCKY"
		self.definitions = [u'having good things happen to you by chance: ', u'bringing good luck: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
