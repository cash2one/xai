

#calss header
class _RUSTPROOF():
	def __init__(self,): 
		self.name = "RUSTPROOF"
		self.definitions = [u'protected against rust (= metal decay)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
