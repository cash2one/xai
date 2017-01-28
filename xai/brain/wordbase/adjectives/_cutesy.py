

#calss header
class _CUTESY():
	def __init__(self,): 
		self.name = "CUTESY"
		self.definitions = [u'artificially attractive and pleasant, especially in a childish way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
