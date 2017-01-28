

#calss header
class _SIDEREAL():
	def __init__(self,): 
		self.name = "SIDEREAL"
		self.definitions = [u'of or calculated by the stars']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
