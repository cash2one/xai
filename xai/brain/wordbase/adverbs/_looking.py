

#calss header
class _LOOKING():
	def __init__(self,): 
		self.name = "LOOKING"
		self.definitions = [u'having the stated appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
