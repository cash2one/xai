

#calss header
class _WATERPROOF():
	def __init__(self,): 
		self.name = "WATERPROOF"
		self.definitions = [u'not allowing water to go through: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
