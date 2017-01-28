

#calss header
class _WOEFULLY():
	def __init__(self,): 
		self.name = "WOEFULLY"
		self.definitions = [u'used to emphasize how bad a situation is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
