

#calss header
class _COBALT():
	def __init__(self,): 
		self.name = "COBALT"
		self.definitions = [u'having a deep blue or greenish-blue colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
