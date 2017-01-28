

#calss header
class _BRIEFLY():
	def __init__(self,): 
		self.name = "BRIEFLY"
		self.definitions = [u'for a short time: ', u'using few words or without giving a lot of details: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
