

#calss header
class _IMPERVIOUS():
	def __init__(self,): 
		self.name = "IMPERVIOUS"
		self.definitions = [u'not allowing liquid to go through: ', u'If someone is impervious to something,they are not influenced or affected by something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
