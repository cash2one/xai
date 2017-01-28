

#calss header
class _UNIQUE():
	def __init__(self,): 
		self.name = "UNIQUE"
		self.definitions = [u'being the only existing one of its type or, more generally, unusual, or special in some way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
