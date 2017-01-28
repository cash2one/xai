

#calss header
class _UNFORGIVABLE():
	def __init__(self,): 
		self.name = "UNFORGIVABLE"
		self.definitions = [u'(of behaviour) too bad to forgive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
