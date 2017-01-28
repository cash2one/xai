

#calss header
class _COSILY():
	def __init__(self,): 
		self.name = "COSILY"
		self.definitions = [u'in a comfortable, warm, and pleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
