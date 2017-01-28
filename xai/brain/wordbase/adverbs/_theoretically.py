

#calss header
class _THEORETICALLY():
	def __init__(self,): 
		self.name = "THEORETICALLY"
		self.definitions = [u'in a way that obeys some rules but is not likely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
