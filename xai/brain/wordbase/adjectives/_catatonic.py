

#calss header
class _CATATONIC():
	def __init__(self,): 
		self.name = "CATATONIC"
		self.definitions = [u'If someone is catatonic, they are stiff and not moving or reacting, as if dead.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
