

#calss header
class _PARAMOUNT():
	def __init__(self,): 
		self.name = "PARAMOUNT"
		self.definitions = [u'more important than anything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
