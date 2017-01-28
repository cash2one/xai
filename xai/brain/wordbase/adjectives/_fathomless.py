

#calss header
class _FATHOMLESS():
	def __init__(self,): 
		self.name = "FATHOMLESS"
		self.definitions = [u'too deep to be measured: ', u'impossible to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
