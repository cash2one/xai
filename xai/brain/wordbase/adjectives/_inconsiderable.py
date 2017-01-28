

#calss header
class _INCONSIDERABLE():
	def __init__(self,): 
		self.name = "INCONSIDERABLE"
		self.definitions = [u'very small and therefore not important or not worth considering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
