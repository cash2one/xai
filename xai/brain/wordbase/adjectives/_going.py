

#calss header
class _GOING():
	def __init__(self,): 
		self.name = "GOING"
		self.definitions = [u'available or existing: ', u'the usual rate, price, etc. at a particular time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
