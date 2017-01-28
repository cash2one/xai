

#calss header
class _ORIGINALLY():
	def __init__(self,): 
		self.name = "ORIGINALLY"
		self.definitions = [u'first of all: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
