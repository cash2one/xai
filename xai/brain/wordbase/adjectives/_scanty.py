

#calss header
class _SCANTY():
	def __init__(self,): 
		self.name = "SCANTY"
		self.definitions = [u'smaller in size or amount than is considered necessary or is hoped for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
