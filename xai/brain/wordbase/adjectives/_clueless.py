

#calss header
class _CLUELESS():
	def __init__(self,): 
		self.name = "CLUELESS"
		self.definitions = [u'having no knowledge of something, or of things in general: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
