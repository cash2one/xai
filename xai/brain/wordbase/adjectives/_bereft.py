

#calss header
class _BEREFT():
	def __init__(self,): 
		self.name = "BEREFT"
		self.definitions = [u'not having something or feeling great loss: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
