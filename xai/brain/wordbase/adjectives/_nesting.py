

#calss header
class _NESTING():
	def __init__(self,): 
		self.name = "NESTING"
		self.definitions = [u'fitting inside each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
