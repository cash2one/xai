

#calss header
class _CONSUMABLE():
	def __init__(self,): 
		self.name = "CONSUMABLE"
		self.definitions = [u'bought regularly because of being quickly used and needing to be replaced often: ', u'possible to eat, drink, or use up completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
