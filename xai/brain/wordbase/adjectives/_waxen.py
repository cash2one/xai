

#calss header
class _WAXEN():
	def __init__(self,): 
		self.name = "WAXEN"
		self.definitions = [u'A waxen face has pale, shiny skin and does not look healthy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
