

#calss header
class _DAINTY():
	def __init__(self,): 
		self.name = "DAINTY"
		self.definitions = [u'small, delicate, and often moving in a careful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
