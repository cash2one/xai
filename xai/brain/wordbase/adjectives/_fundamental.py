

#calss header
class _FUNDAMENTAL():
	def __init__(self,): 
		self.name = "FUNDAMENTAL"
		self.definitions = [u'forming the base, from which everything else develops: ', u'more important than anything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
