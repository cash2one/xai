

#calss header
class _SPARTAN():
	def __init__(self,): 
		self.name = "SPARTAN"
		self.definitions = [u'simple and severe with no comfort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
