

#calss header
class _TRANSATLANTIC():
	def __init__(self,): 
		self.name = "TRANSATLANTIC"
		self.definitions = [u'crossing the Atlantic ocean, or relating to countries on both sides of the Atlantic Ocean: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
