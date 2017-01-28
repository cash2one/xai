

#calss header
class _CONDESCENDING():
	def __init__(self,): 
		self.name = "CONDESCENDING"
		self.definitions = [u'treating someone as if you are more important or more intelligent than them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
