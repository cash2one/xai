

#calss header
class _UNPRETENTIOUS():
	def __init__(self,): 
		self.name = "UNPRETENTIOUS"
		self.definitions = [u'simple and/or sincere; not pretentious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
