

#calss header
class _DISORDERED():
	def __init__(self,): 
		self.name = "DISORDERED"
		self.definitions = [u'not normal, in a way that is unhealthy: ', u'in a confused or badly organized state: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
