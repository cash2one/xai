

#calss header
class _RANGY():
	def __init__(self,): 
		self.name = "RANGY"
		self.definitions = [u'having long thin legs and arms: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
