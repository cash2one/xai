

#calss header
class _SLAPHAPPY():
	def __init__(self,): 
		self.name = "SLAPHAPPY"
		self.definitions = [u'happily careless and not thinking about the results of your actions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
