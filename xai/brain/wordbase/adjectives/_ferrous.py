

#calss header
class _FERROUS():
	def __init__(self,): 
		self.name = "FERROUS"
		self.definitions = [u'containing or relating to iron: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
