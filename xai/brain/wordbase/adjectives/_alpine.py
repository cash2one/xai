

#calss header
class _ALPINE():
	def __init__(self,): 
		self.name = "ALPINE"
		self.definitions = [u'relating to the Alps: ', u'relating to high mountain areas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
