

#calss header
class _HETEROGENEOUS():
	def __init__(self,): 
		self.name = "HETEROGENEOUS"
		self.definitions = [u'consisting of parts or things that are very different from each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
