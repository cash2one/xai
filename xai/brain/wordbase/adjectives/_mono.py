

#calss header
class _MONO():
	def __init__(self,): 
		self.name = "MONO"
		self.definitions = [u'Mono sound is recorded or broadcast sound that comes from a single direction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
