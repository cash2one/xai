

#calss header
class _SUBSTANDARD():
	def __init__(self,): 
		self.name = "SUBSTANDARD"
		self.definitions = [u'below a satisfactory standard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
