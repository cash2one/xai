

#calss header
class _TRITE():
	def __init__(self,): 
		self.name = "TRITE"
		self.definitions = [u'expressed too often to be interesting or seem sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
