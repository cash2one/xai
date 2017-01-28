

#calss header
class _BLOODSHOT():
	def __init__(self,): 
		self.name = "BLOODSHOT"
		self.definitions = [u'When your eyes are bloodshot, they are red or pink on the white parts.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
