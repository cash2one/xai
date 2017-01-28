

#calss header
class _REPRESSED():
	def __init__(self,): 
		self.name = "REPRESSED"
		self.definitions = [u'having feelings that you do not express: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
