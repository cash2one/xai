

#calss header
class _FUSED():
	def __init__(self,): 
		self.name = "FUSED"
		self.definitions = [u'An electrical device or a piece of machinery that is fused has a fuse in it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
