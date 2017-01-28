

#calss header
class _PREDOMINANTLY():
	def __init__(self,): 
		self.name = "PREDOMINANTLY"
		self.definitions = [u'mostly or mainly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
