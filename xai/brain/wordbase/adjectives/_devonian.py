

#calss header
class _DEVONIAN():
	def __init__(self,): 
		self.name = "DEVONIAN"
		self.definitions = [u'from or referring to the period of time between about 420 and 360 million years ago, in which many plants, including the first trees, appeared on land: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
