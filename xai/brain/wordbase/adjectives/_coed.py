

#calss header
class _COED():
	def __init__(self,): 
		self.name = "COED"
		self.definitions = [u'informal for  coeducational ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
