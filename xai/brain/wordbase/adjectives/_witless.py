

#calss header
class _WITLESS():
	def __init__(self,): 
		self.name = "WITLESS"
		self.definitions = [u'stupid or showing no intelligence: ', u'to frighten someone very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
