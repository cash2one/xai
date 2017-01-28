

#calss header
class _CERTAIN():
	def __init__(self,): 
		self.name = "CERTAIN"
		self.definitions = [u'particular but not named or described: ', u'used before a noun when it is difficult to describe something exactly or give its exact amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
