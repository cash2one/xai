

#calss header
class _BLUISH():
	def __init__(self,): 
		self.name = "BLUISH"
		self.definitions = [u'slightly blue: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
