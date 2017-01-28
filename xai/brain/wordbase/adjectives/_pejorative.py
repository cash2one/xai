

#calss header
class _PEJORATIVE():
	def __init__(self,): 
		self.name = "PEJORATIVE"
		self.definitions = [u'expressing disapproval, or suggesting that something is not good or is of no importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
