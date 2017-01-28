

#calss header
class _ALIVE():
	def __init__(self,): 
		self.name = "ALIVE"
		self.definitions = [u'living, not dead: ', u'If something is alive, it continues to exist: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
