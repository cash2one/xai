

#calss header
class _TORCHLIGHT():
	def __init__(self,): 
		self.name = "TORCHLIGHT"
		self.definitions = [u'A torchlight event is one that is lit by burning torches: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
