

#calss header
class _WAVY():
	def __init__(self,): 
		self.name = "WAVY"
		self.definitions = [u'having a series of curves: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
