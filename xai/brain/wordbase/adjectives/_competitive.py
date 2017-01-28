

#calss header
class _COMPETITIVE():
	def __init__(self,): 
		self.name = "COMPETITIVE"
		self.definitions = [u'involving competition: ', u'wanting very much to win or be more successful than other people: ', u'Competitive prices, services, etc. are as good as or better than other prices, services, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
