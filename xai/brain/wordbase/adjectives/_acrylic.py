

#calss header
class _ACRYLIC():
	def __init__(self,): 
		self.name = "ACRYLIC"
		self.definitions = [u'made of a substance or cloth produced by chemical processes from a type of acid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
