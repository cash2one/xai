

#calss header
class _MINT():
	def __init__(self,): 
		self.name = "MINT"
		self.definitions = [u'Mint stamps and coins, etc. have not been used: ', u'perfect, as if new: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
