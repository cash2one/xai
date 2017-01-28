

#calss header
class _FAVORABLE():
	def __init__(self,): 
		self.name = "FAVORABLE"
		self.definitions = [u'US spelling of  favourable ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
