

#calss header
class _PENURIOUS():
	def __init__(self,): 
		self.name = "PENURIOUS"
		self.definitions = [u'extremely poor']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
