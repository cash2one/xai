

#calss header
class _GEODESIC():
	def __init__(self,): 
		self.name = "GEODESIC"
		self.definitions = [u'relating to the shortest possible line between two points on a sphere or other curved surface']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
