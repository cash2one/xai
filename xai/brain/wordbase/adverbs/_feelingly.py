

#calss header
class _FEELINGLY():
	def __init__(self,): 
		self.name = "FEELINGLY"
		self.definitions = [u'with deep and sincere emotion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
