

#calss header
class _COLLOQUIAL():
	def __init__(self,): 
		self.name = "COLLOQUIAL"
		self.definitions = [u'(of words and expressions) informal and more suitable for use in speech than in writing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
