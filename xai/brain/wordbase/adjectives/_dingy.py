

#calss header
class _DINGY():
	def __init__(self,): 
		self.name = "DINGY"
		self.definitions = [u'dark and often also dirty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
