

#calss header
class _ACRID():
	def __init__(self,): 
		self.name = "ACRID"
		self.definitions = [u'An acrid smell or taste is strong and bitter and causes a burning feeling in the throat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
