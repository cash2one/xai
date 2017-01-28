

#calss header
class _GALLIC():
	def __init__(self,): 
		self.name = "GALLIC"
		self.definitions = [u'French or typically French: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
