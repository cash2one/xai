

#calss header
class _AGRARIAN():
	def __init__(self,): 
		self.name = "AGRARIAN"
		self.definitions = [u'relating to the land, especially the use of land for farming: ', u'An agrarian place or country makes its money from farming rather than industry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
