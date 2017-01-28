

#calss header
class _LOWBROW():
	def __init__(self,): 
		self.name = "LOWBROW"
		self.definitions = [u'(of entertainment) not complicated or demanding much intelligence to be understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
