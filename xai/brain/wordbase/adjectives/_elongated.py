

#calss header
class _ELONGATED():
	def __init__(self,): 
		self.name = "ELONGATED"
		self.definitions = [u'longer and thinner than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
