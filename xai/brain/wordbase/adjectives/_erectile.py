

#calss header
class _ERECTILE():
	def __init__(self,): 
		self.name = "ERECTILE"
		self.definitions = [u'Erectile body tissue is able to become larger and harder than usual by being filled with blood.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
