

#calss header
class _EGALITARIAN():
	def __init__(self,): 
		self.name = "EGALITARIAN"
		self.definitions = [u'believing that all people are equally important and should have the same rights and opportunities in life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
