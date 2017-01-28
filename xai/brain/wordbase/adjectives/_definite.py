

#calss header
class _DEFINITE():
	def __init__(self,): 
		self.name = "DEFINITE"
		self.definitions = [u'fixed, certain, or clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
