

#calss header
class _CARTILAGINOUS():
	def __init__(self,): 
		self.name = "CARTILAGINOUS"
		self.definitions = [u'relating to or consisting of cartilage (= the strong stretchy tissue found in the joints): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
