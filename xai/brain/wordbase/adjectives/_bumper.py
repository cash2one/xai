

#calss header
class _BUMPER():
	def __init__(self,): 
		self.name = "BUMPER"
		self.definitions = [u'larger in amount than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
