

#calss header
class _PROPORTIONED():
	def __init__(self,): 
		self.name = "PROPORTIONED"
		self.definitions = [u'having parts of the size or shape that is described: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
