

#calss header
class _TALL():
	def __init__(self,): 
		self.name = "TALL"
		self.definitions = [u'of more than average height, or of a particular height: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
