

#calss header
class _PREFATORY():
	def __init__(self,): 
		self.name = "PREFATORY"
		self.definitions = [u'coming at the beginning of a piece of writing or a speech: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
