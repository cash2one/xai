

#calss header
class _HOMESPUN():
	def __init__(self,): 
		self.name = "HOMESPUN"
		self.definitions = [u'(of beliefs, theories, etc.) simple and ordinary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
