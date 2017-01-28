

#calss header
class _BOVINE():
	def __init__(self,): 
		self.name = "BOVINE"
		self.definitions = [u'connected with cows: ', u'slow or stupid in a way that a cow is thought to be: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
