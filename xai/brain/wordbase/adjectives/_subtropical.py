

#calss header
class _SUBTROPICAL():
	def __init__(self,): 
		self.name = "SUBTROPICAL"
		self.definitions = [u'belonging to or relating to parts of the world that are immediately south or north of the tropics (= the hottest areas) and have very hot weather at some times of the year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
