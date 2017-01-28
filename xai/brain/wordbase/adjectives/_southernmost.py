

#calss header
class _SOUTHERNMOST():
	def __init__(self,): 
		self.name = "SOUTHERNMOST"
		self.definitions = [u'furthest towards the south of an area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
