

#calss header
class _SPRUCE():
	def __init__(self,): 
		self.name = "SPRUCE"
		self.definitions = [u'(of a person) tidy and clean in appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
