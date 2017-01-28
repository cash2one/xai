

#calss header
class _GALACTIC():
	def __init__(self,): 
		self.name = "GALACTIC"
		self.definitions = [u'relating to the Galaxy or other galaxies: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
