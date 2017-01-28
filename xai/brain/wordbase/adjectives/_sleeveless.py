

#calss header
class _SLEEVELESS():
	def __init__(self,): 
		self.name = "SLEEVELESS"
		self.definitions = [u'A sleeveless piece of clothing has no sleeves: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
