

#calss header
class _INDEFENSIBLE():
	def __init__(self,): 
		self.name = "INDEFENSIBLE"
		self.definitions = [u'too bad to be protected from criticism: ', u'not able to be protected against attack: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
