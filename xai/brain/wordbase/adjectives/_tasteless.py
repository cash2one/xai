

#calss header
class _TASTELESS():
	def __init__(self,): 
		self.name = "TASTELESS"
		self.definitions = [u'likely to upset someone: ', u'having no flavour: ', u'not stylish: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
