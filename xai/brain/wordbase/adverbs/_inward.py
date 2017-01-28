

#calss header
class _INWARD():
	def __init__(self,): 
		self.name = "INWARD"
		self.definitions = [u' inwards ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
