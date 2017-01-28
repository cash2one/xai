

#calss header
class _BUSTED():
	def __init__(self,): 
		self.name = "BUSTED"
		self.definitions = [u'broken: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
