

#calss header
class _DOUBTLESS():
	def __init__(self,): 
		self.name = "DOUBTLESS"
		self.definitions = [u'used to mean that you are certain that something will happen or is true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
