

#calss header
class _STRAPPING():
	def __init__(self,): 
		self.name = "STRAPPING"
		self.definitions = [u'A strapping person is tall and strong-looking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
