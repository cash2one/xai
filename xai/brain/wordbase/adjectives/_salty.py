

#calss header
class _SALTY():
	def __init__(self,): 
		self.name = "SALTY"
		self.definitions = [u'tasting of salt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
