

#calss header
class _SUPREME():
	def __init__(self,): 
		self.name = "SUPREME"
		self.definitions = [u'having the highest rank, level, or importance: ', u'very great, or the best: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
