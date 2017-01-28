

#calss header
class _UNEMOTIONAL():
	def __init__(self,): 
		self.name = "UNEMOTIONAL"
		self.definitions = [u'not having or expressing strong feelings, often when this is surprising or a bad thing: ', u'not allowing strong feelings to influence your decisions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
