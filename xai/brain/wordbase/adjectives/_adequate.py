

#calss header
class _ADEQUATE():
	def __init__(self,): 
		self.name = "ADEQUATE"
		self.definitions = [u'enough or satisfactory for a particular purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
