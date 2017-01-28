

#calss header
class _UNISEX():
	def __init__(self,): 
		self.name = "UNISEX"
		self.definitions = [u'intended for use by both males and females: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
