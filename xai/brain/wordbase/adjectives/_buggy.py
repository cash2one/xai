

#calss header
class _BUGGY():
	def __init__(self,): 
		self.name = "BUGGY"
		self.definitions = [u'full of annoying bugs: ', u'Computer programs that are buggy contain mistakes and do no work correctly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
