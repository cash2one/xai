

#calss header
class _BOUNTIFUL():
	def __init__(self,): 
		self.name = "BOUNTIFUL"
		self.definitions = [u'large in amount: ', u'generous in giving to others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
