

#calss header
class _PROUD():
	def __init__(self,): 
		self.name = "PROUD"
		self.definitions = [u'sticking out from the surrounding area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
