

#calss header
class _AQUATIC():
	def __init__(self,): 
		self.name = "AQUATIC"
		self.definitions = [u'living or growing in, happening in, or connected with water: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
