

#calss header
class _UNCHALLENGED():
	def __init__(self,): 
		self.name = "UNCHALLENGED"
		self.definitions = [u'accepted without asking questions or criticizing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
