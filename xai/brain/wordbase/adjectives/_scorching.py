

#calss header
class _SCORCHING():
	def __init__(self,): 
		self.name = "SCORCHING"
		self.definitions = [u'very hot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
