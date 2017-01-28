

#calss header
class _INVULNERABLE():
	def __init__(self,): 
		self.name = "INVULNERABLE"
		self.definitions = [u'impossible to damage or hurt in any way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
