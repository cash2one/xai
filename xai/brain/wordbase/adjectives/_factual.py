

#calss header
class _FACTUAL():
	def __init__(self,): 
		self.name = "FACTUAL"
		self.definitions = [u'using or consisting of facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
