

#calss header
class _INCREASINGLY():
	def __init__(self,): 
		self.name = "INCREASINGLY"
		self.definitions = [u'more and more: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
