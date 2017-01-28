

#calss header
class _INGENUOUS():
	def __init__(self,): 
		self.name = "INGENUOUS"
		self.definitions = [u'honest, sincere, and trusting, sometimes in a way that seems silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
