

#calss header
class _DERISORY():
	def __init__(self,): 
		self.name = "DERISORY"
		self.definitions = [u'A derisory amount of money is so small it is silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
