

#calss header
class _MAROONED():
	def __init__(self,): 
		self.name = "MAROONED"
		self.definitions = [u'left in a place from which you cannot escape: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
