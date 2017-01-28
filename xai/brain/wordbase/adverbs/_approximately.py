

#calss header
class _APPROXIMATELY():
	def __init__(self,): 
		self.name = "APPROXIMATELY"
		self.definitions = [u'close to a particular number or time although not exactly that number or time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
