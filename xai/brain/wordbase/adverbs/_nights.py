

#calss header
class _NIGHTS():
	def __init__(self,): 
		self.name = "NIGHTS"
		self.definitions = [u'at night, especially every night: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
