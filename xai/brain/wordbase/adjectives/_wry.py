

#calss header
class _WRY():
	def __init__(self,): 
		self.name = "WRY"
		self.definitions = [u'showing that you find a bad or difficult situation slightly funny: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
