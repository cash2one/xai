

#calss header
class _MINERAL():
	def __init__(self,): 
		self.name = "MINERAL"
		self.definitions = [u'being or consisting of a mineral or minerals: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
