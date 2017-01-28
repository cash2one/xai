

#calss header
class _ASCETIC():
	def __init__(self,): 
		self.name = "ASCETIC"
		self.definitions = [u'avoiding physical pleasures and living a simple life, often for religious reasons: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
