

#calss header
class _PERPETUAL():
	def __init__(self,): 
		self.name = "PERPETUAL"
		self.definitions = [u'continuing for ever in the same way: ', u'often repeated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
