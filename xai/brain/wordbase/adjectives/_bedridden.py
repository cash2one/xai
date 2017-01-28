

#calss header
class _BEDRIDDEN():
	def __init__(self,): 
		self.name = "BEDRIDDEN"
		self.definitions = [u'having to stay in bed because of illness or injury: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
