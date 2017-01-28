

#calss header
class _BASICALLY():
	def __init__(self,): 
		self.name = "BASICALLY"
		self.definitions = [u'used when referring to the main or most important characteristic or feature of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
