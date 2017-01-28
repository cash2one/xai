

#calss header
class _PURPOSELESS():
	def __init__(self,): 
		self.name = "PURPOSELESS"
		self.definitions = [u'done without a clear intention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
