

#calss header
class _WINGED():
	def __init__(self,): 
		self.name = "WINGED"
		self.definitions = [u'having the stated type of wings: ', u'with wings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
