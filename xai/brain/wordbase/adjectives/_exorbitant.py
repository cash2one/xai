

#calss header
class _EXORBITANT():
	def __init__(self,): 
		self.name = "EXORBITANT"
		self.definitions = [u'Exorbitant prices, demands, etc. are much too large: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
