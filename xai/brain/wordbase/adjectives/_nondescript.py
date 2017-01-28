

#calss header
class _NONDESCRIPT():
	def __init__(self,): 
		self.name = "NONDESCRIPT"
		self.definitions = [u'very ordinary, or having no interesting or exciting features or qualities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
