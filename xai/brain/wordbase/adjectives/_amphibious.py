

#calss header
class _AMPHIBIOUS():
	def __init__(self,): 
		self.name = "AMPHIBIOUS"
		self.definitions = [u'of or relating to a type of animal that lives both on land and in water: ', u'relating to vehicles that operate both on land and in water: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
