

#calss header
class _UNSIGHTLY():
	def __init__(self,): 
		self.name = "UNSIGHTLY"
		self.definitions = [u'not attractive; ugly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
