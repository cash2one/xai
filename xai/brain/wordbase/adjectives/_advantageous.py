

#calss header
class _ADVANTAGEOUS():
	def __init__(self,): 
		self.name = "ADVANTAGEOUS"
		self.definitions = [u'giving advantages or helping to make you more successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
