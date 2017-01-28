

#calss header
class _BLUFF():
	def __init__(self,): 
		self.name = "BLUFF"
		self.definitions = [u'direct or too honest, often in a way that people find rude: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
