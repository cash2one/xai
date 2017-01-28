

#calss header
class _UNSIGNED():
	def __init__(self,): 
		self.name = "UNSIGNED"
		self.definitions = [u'(of a letter, painting, etc.) with no name or signature on it, saying who has written or painted it: ', u'not having signed a contract (= a legal document stating a formal agreement) of employment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
