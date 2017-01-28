

#calss header
class _CALLOUS():
	def __init__(self,): 
		self.name = "CALLOUS"
		self.definitions = [u'unkind, cruel, and without sympathy or feeling for other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
