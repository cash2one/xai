

#calss header
class _EARTHEN():
	def __init__(self,): 
		self.name = "EARTHEN"
		self.definitions = [u'made of earth or of baked clay: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
