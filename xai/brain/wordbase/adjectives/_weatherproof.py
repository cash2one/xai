

#calss header
class _WEATHERPROOF():
	def __init__(self,): 
		self.name = "WEATHERPROOF"
		self.definitions = [u'not allowing wind or rain to go through: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
