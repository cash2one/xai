

#calss header
class _FANTASTIC():
	def __init__(self,): 
		self.name = "FANTASTIC"
		self.definitions = [u'extremely good: ', u'strange and imaginary, or not reasonable: ', u'very unusual, strange, or unexpected: ', u'A fantastic amount is very large: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
