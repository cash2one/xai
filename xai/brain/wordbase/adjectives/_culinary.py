

#calss header
class _CULINARY():
	def __init__(self,): 
		self.name = "CULINARY"
		self.definitions = [u'connected with cooking or kitchens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
