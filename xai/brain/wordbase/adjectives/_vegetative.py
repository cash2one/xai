

#calss header
class _VEGETATIVE():
	def __init__(self,): 
		self.name = "VEGETATIVE"
		self.definitions = [u'alive but showing no brain activity']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
