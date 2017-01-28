

#calss header
class _SORTED():
	def __init__(self,): 
		self.name = "SORTED"
		self.definitions = [u'used to describe a situation in which everything is correctly organized or repaired, or when someone has everything that is needed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
