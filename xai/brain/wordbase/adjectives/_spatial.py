

#calss header
class _SPATIAL():
	def __init__(self,): 
		self.name = "SPATIAL"
		self.definitions = [u'relating to the position, area, and size of things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
