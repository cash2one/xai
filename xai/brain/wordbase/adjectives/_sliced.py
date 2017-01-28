

#calss header
class _SLICED():
	def __init__(self,): 
		self.name = "SLICED"
		self.definitions = [u'cut into thin, flat pieces: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
