

#calss header
class _SYNTHETIC():
	def __init__(self,): 
		self.name = "SYNTHETIC"
		self.definitions = [u'Synthetic products are made from artificial substances, often copying a natural product: ', u'false or artificial: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
