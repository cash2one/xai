

#calss header
class _BENIGHTED():
	def __init__(self,): 
		self.name = "BENIGHTED"
		self.definitions = [u'without knowledge or morals: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
