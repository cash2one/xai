

#calss header
class _SMASHED():
	def __init__(self,): 
		self.name = "SMASHED"
		self.definitions = [u'extremely drunk, or powerfully affected by illegal drugs']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
