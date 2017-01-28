

#calss header
class _REMISS():
	def __init__(self,): 
		self.name = "REMISS"
		self.definitions = [u'careless and not doing a duty well enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
