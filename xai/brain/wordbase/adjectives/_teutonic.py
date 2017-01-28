

#calss header
class _TEUTONIC():
	def __init__(self,): 
		self.name = "TEUTONIC"
		self.definitions = [u'of, or thought to be typical of, the groups of people in northwestern Europe of German origin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
