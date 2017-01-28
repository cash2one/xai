

#calss header
class _OVAL():
	def __init__(self,): 
		self.name = "OVAL"
		self.definitions = [u'shaped like a circle that is flattened so that it is like an egg or an ellipse: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
