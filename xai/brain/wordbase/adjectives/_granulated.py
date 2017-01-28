

#calss header
class _GRANULATED():
	def __init__(self,): 
		self.name = "GRANULATED"
		self.definitions = [u'in small grains: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
