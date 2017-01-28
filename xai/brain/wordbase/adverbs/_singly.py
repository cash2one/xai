

#calss header
class _SINGLY():
	def __init__(self,): 
		self.name = "SINGLY"
		self.definitions = [u'one at a time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
