

#calss header
class _PASSIONATE():
	def __init__(self,): 
		self.name = "PASSIONATE"
		self.definitions = [u'having very strong feelings or emotions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
