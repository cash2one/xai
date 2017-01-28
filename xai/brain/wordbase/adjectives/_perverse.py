

#calss header
class _PERVERSE():
	def __init__(self,): 
		self.name = "PERVERSE"
		self.definitions = [u'strange and not what most people would expect or enjoy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
