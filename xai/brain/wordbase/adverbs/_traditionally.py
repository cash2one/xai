

#calss header
class _TRADITIONALLY():
	def __init__(self,): 
		self.name = "TRADITIONALLY"
		self.definitions = [u'according to tradition; in a traditional way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
