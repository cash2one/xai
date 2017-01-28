

#calss header
class _NEVER():
	def __init__(self,): 
		self.name = "NEVER"
		self.definitions = [u'not at any time or not on any occasion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
