

#calss header
class _AMBIGUOUS():
	def __init__(self,): 
		self.name = "AMBIGUOUS"
		self.definitions = [u'having or expressing more than one possible meaning, sometimes intentionally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
