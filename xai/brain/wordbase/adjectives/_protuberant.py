

#calss header
class _PROTUBERANT():
	def __init__(self,): 
		self.name = "PROTUBERANT"
		self.definitions = [u'sticking out: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
