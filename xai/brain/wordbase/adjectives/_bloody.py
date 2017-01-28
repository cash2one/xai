

#calss header
class _BLOODY():
	def __init__(self,): 
		self.name = "BLOODY"
		self.definitions = [u'used to express anger or to emphasize what you are saying in a slightly rude way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
