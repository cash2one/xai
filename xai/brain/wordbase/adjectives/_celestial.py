

#calss header
class _CELESTIAL():
	def __init__(self,): 
		self.name = "CELESTIAL"
		self.definitions = [u'of or from the sky or outside this world: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
