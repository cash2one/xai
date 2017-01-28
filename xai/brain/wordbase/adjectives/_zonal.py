

#calss header
class _ZONAL():
	def __init__(self,): 
		self.name = "ZONAL"
		self.definitions = [u'relating to or arranged in zones: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
