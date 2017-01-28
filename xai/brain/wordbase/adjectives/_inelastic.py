

#calss header
class _INELASTIC():
	def __init__(self,): 
		self.name = "INELASTIC"
		self.definitions = [u'not changing much, or not allowing much change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
