

#calss header
class _DRINKABLE():
	def __init__(self,): 
		self.name = "DRINKABLE"
		self.definitions = [u'clean and safe to drink: ', u'pleasant tasting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
