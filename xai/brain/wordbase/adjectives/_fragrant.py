

#calss header
class _FRAGRANT():
	def __init__(self,): 
		self.name = "FRAGRANT"
		self.definitions = [u'with a pleasant smell: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
