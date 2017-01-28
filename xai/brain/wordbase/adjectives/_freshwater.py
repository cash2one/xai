

#calss header
class _FRESHWATER():
	def __init__(self,): 
		self.name = "FRESHWATER"
		self.definitions = [u'living in or containing water that is not salty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
