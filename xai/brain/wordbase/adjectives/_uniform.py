

#calss header
class _UNIFORM():
	def __init__(self,): 
		self.name = "UNIFORM"
		self.definitions = [u'the same; not changing or different in any way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
