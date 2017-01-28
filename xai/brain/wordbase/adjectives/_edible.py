

#calss header
class _EDIBLE():
	def __init__(self,): 
		self.name = "EDIBLE"
		self.definitions = [u'suitable or safe for eating: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
