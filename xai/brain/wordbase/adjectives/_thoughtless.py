

#calss header
class _THOUGHTLESS():
	def __init__(self,): 
		self.name = "THOUGHTLESS"
		self.definitions = [u'not considering how your actions or words may upset someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
