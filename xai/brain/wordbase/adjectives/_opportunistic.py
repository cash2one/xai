

#calss header
class _OPPORTUNISTIC():
	def __init__(self,): 
		self.name = "OPPORTUNISTIC"
		self.definitions = [u'using a situation to get power or an advantage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
