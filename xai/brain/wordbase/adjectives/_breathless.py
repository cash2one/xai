

#calss header
class _BREATHLESS():
	def __init__(self,): 
		self.name = "BREATHLESS"
		self.definitions = [u'not able to breathe easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
