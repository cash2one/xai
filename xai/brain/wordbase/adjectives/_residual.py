

#calss header
class _RESIDUAL():
	def __init__(self,): 
		self.name = "RESIDUAL"
		self.definitions = [u'remaining after most of something has gone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
