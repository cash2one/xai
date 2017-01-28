

#calss header
class _EASTERNMOST():
	def __init__(self,): 
		self.name = "EASTERNMOST"
		self.definitions = [u'furthest towards the east of an area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
