

#calss header
class _UNCEASING():
	def __init__(self,): 
		self.name = "UNCEASING"
		self.definitions = [u'continuing and unlikely to stop or become less: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
