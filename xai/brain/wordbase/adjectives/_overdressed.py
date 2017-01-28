

#calss header
class _OVERDRESSED():
	def __init__(self,): 
		self.name = "OVERDRESSED"
		self.definitions = [u'wearing clothes that are too formal or special for a particular occasion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
