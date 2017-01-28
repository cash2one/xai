

#calss header
class _UTILITARIAN():
	def __init__(self,): 
		self.name = "UTILITARIAN"
		self.definitions = [u'designed to be useful rather than decorative: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
