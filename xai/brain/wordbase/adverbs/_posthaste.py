

#calss header
class _POSTHASTE():
	def __init__(self,): 
		self.name = "POSTHASTE"
		self.definitions = [u'as fast as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
