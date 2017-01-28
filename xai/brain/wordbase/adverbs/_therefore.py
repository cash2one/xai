

#calss header
class _THEREFORE():
	def __init__(self,): 
		self.name = "THEREFORE"
		self.definitions = [u'for that reason: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
