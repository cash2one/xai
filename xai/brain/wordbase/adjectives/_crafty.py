

#calss header
class _CRAFTY():
	def __init__(self,): 
		self.name = "CRAFTY"
		self.definitions = [u'clever, especially in a dishonest or secret way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
