

#calss header
class _STATISTICAL():
	def __init__(self,): 
		self.name = "STATISTICAL"
		self.definitions = [u'relating to statistics: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
