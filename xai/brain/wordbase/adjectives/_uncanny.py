

#calss header
class _UNCANNY():
	def __init__(self,): 
		self.name = "UNCANNY"
		self.definitions = [u'strange or mysterious; difficult or impossible to explain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
