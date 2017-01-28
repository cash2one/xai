

#calss header
class _WESTERNMOST():
	def __init__(self,): 
		self.name = "WESTERNMOST"
		self.definitions = [u'furthest towards the west of an area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
