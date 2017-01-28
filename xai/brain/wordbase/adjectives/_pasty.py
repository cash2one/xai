

#calss header
class _PASTY():
	def __init__(self,): 
		self.name = "PASTY"
		self.definitions = [u"(of someone's face or skin) very pale and unhealthy looking: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
