

#calss header
class _LOGICAL():
	def __init__(self,): 
		self.name = "LOGICAL"
		self.definitions = [u'using reason: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
