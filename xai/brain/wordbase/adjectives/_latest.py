

#calss header
class _LATEST():
	def __init__(self,): 
		self.name = "LATEST"
		self.definitions = [u'newest or most recent or modern: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
