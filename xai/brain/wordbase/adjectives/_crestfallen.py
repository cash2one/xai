

#calss header
class _CRESTFALLEN():
	def __init__(self,): 
		self.name = "CRESTFALLEN"
		self.definitions = [u'disappointed and sad because of having failed unexpectedly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
