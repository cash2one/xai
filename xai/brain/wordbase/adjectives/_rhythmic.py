

#calss header
class _RHYTHMIC():
	def __init__(self,): 
		self.name = "RHYTHMIC"
		self.definitions = [u'A rhythmic sound has a regular movement or beat that is repeated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
