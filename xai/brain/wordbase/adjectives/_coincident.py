

#calss header
class _COINCIDENT():
	def __init__(self,): 
		self.name = "COINCIDENT"
		self.definitions = [u'happening at the same time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
