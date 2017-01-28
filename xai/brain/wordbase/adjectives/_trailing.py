

#calss header
class _TRAILING():
	def __init__(self,): 
		self.name = "TRAILING"
		self.definitions = [u'Trailing plants grow along the ground or over the surface of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
