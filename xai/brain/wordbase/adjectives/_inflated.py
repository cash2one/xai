

#calss header
class _INFLATED():
	def __init__(self,): 
		self.name = "INFLATED"
		self.definitions = [u'Inflated prices, costs, numbers, etc. are higher than they should be, or higher than people think is reasonable.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
