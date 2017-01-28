

#calss header
class _OPERATIC():
	def __init__(self,): 
		self.name = "OPERATIC"
		self.definitions = [u'of, for, or relating to opera: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
