

#calss header
class _SIMILAR():
	def __init__(self,): 
		self.name = "SIMILAR"
		self.definitions = [u'looking or being almost, but not exactly, the same: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
