

#calss header
class _MATCHLESS():
	def __init__(self,): 
		self.name = "MATCHLESS"
		self.definitions = [u'of a very high standard or quality and better than everything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
