

#calss header
class _SKINLESS():
	def __init__(self,): 
		self.name = "SKINLESS"
		self.definitions = [u'without a skin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
