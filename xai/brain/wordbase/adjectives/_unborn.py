

#calss header
class _UNBORN():
	def __init__(self,): 
		self.name = "UNBORN"
		self.definitions = [u"not yet born; in the mother's womb: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
