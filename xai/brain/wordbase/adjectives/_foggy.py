

#calss header
class _FOGGY():
	def __init__(self,): 
		self.name = "FOGGY"
		self.definitions = [u'with fog: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
