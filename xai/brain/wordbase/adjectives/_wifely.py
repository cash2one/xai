

#calss header
class _WIFELY():
	def __init__(self,): 
		self.name = "WIFELY"
		self.definitions = [u'like a wife or relating to a wife: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
