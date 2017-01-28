

#calss header
class _BEMUSED():
	def __init__(self,): 
		self.name = "BEMUSED"
		self.definitions = [u'slightly confused: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
