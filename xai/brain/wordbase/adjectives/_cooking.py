

#calss header
class _COOKING():
	def __init__(self,): 
		self.name = "COOKING"
		self.definitions = [u'good for cooking with: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
