

#calss header
class _DARKLY():
	def __init__(self,): 
		self.name = "DARKLY"
		self.definitions = [u'in a way that is threatening or frightening: ', u'in a way that has little or no light: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
