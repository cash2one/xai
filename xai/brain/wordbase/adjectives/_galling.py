

#calss header
class _GALLING():
	def __init__(self,): 
		self.name = "GALLING"
		self.definitions = [u'annoying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
