

#calss header
class _TINNED():
	def __init__(self,): 
		self.name = "TINNED"
		self.definitions = [u'Food that is tinned is put in a tin in order to preserve it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
