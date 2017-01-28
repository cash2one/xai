

#calss header
class _UNSUNG():
	def __init__(self,): 
		self.name = "UNSUNG"
		self.definitions = [u'not noticed or praised for hard work, courage, or great achievements: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
