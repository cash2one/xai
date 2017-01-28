

#calss header
class _SMITTEN():
	def __init__(self,): 
		self.name = "SMITTEN"
		self.definitions = [u'having suddenly started to like or love something or someone very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
