

#calss header
class _FLAVOURFUL():
	def __init__(self,): 
		self.name = "FLAVOURFUL"
		self.definitions = [u'full of flavour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
