

#calss header
class _GLANCING():
	def __init__(self,): 
		self.name = "GLANCING"
		self.definitions = [u'hitting quickly and lightly at an angle: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
