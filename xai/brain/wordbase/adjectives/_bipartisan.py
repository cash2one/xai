

#calss header
class _BIPARTISAN():
	def __init__(self,): 
		self.name = "BIPARTISAN"
		self.definitions = [u'supported by or consisting of two political parties: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
