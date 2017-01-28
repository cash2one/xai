

#calss header
class _VEGAN():
	def __init__(self,): 
		self.name = "VEGAN"
		self.definitions = [u'not eating, using, or including any animal products: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
